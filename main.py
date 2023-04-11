import random
import math
import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np

# Positions of cities (x,y)    
cities = [(62, 80), (30, 9), (47, 91), (95, 35), (82, 57), (10, 48), (5, 72), (55, 15), (70, 52), (47, 3)]
# cities = []
# for i in range(10):
# x = random.randint(0, 100)
# y = random.randint(0, 100)
# cities.append((x, y))

print(cities)

pcount = 100  # Particle count
iterations = 100

# Learning factors, usually equal to 2
c1 = 2
c2 = 2
global_positions = [0] * pcount
global_fitness = [0] * pcount
current_fitness_index = 0


# Holds the definition of a particle
class Particle:

    def __init__(self, cities):
        self.cities = cities
        self.position = random.sample(cities, len(cities))  # Generate random list
        self.best = self.position.copy()  # Best position is initialized to starting list
        self.fitness = self.fitness()
        self.velocity = [0] * len(self.position)  # Init wilt 0s

    # Formula for distance between 2 points
    def distance(self, city1, city2):
        return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

    def fitness(self):
        fitness = 0
        for i in range(len(self.position) - 1):
            fitness += self.distance(self.position[i], self.position[i + 1])  # Get distance between each point
        # Get distance from last point to starting point
        fitness += self.distance(self.position[len(self.position) - 1], self.position[0])
        return fitness

    def get_position(self, gbest, c1, c2):
        r1 = random.random()
        r2 = random.random()
        for i in range(len(self.position)):
            self.velocity[i] = self.velocity[i] + c1 * r1 * (self.best[i][0] - self.position[i][0]) + c2 * r2 * (
                    gbest[i][0] - self.position[i][0])
            x = self.position[i][0] + self.velocity[i]  # Add velocity to x coord
            y = self.position[i][1] + self.velocity[i]  # Add velocity to y coord
            x = self.limit_check(x)
            y = self.limit_check(y)
            self.position[i] = (x, y)
            # global_positions.append(self.best)

    def limit_check(self, coord):
        if (coord < 0):
            coord = 0
        elif (coord > 100):
            coord = 100
        return coord


def simulate_PSO(cities, iter, pcount, c1, c2):
    # Initialize each particle
    particles = []
    gbest = None  # Global best
    pbest = 1000000  # Init Fitness value to really high number so first pass will always go through
    for i in range(pcount):
        particles.append(Particle(cities))
    # For each particle: calc fitness value
    # If fitness value is better than the best fitness value  set current value to new best
    for i in range(iter):
        for count, p in enumerate(particles):  # Loop through each particle
            if (p.fitness < pbest):
                pbest = p.fitness
                gbest = p.best.copy()
                # gbest.append(p.position[0])  # Add the starting city to the end
            p.get_position(gbest, c1, c2)
            global_positions[count] = p.best.copy()  # Get all the best routes
            global_fitness[count] = p.fitness
    # global_positions.append(gbest)
    return gbest, pbest


# Start simulation
best, fitness = simulate_PSO(cities, iterations, pcount, c1, c2)

print("best path", best)
print("best fitness", fitness)

plt.rcParams["animation.html"] = "jshtml"
plt.rcParams['figure.dpi'] = 150
plt.ioff()
fig, ax = plt.subplots()

cx = []
cy = []
x = []
y = []

for i in range(len(cities)):
    cx.append(cities[i][0])
    cy.append(cities[i][1])


def animate(t):
    if (t < len(global_positions)):
        for i in range(len(cities)):
            x.append(global_positions[t][i][0])
            y.append(global_positions[t][i][1])

    # print(len(x))
    plt.cla()
    plt.scatter(x, y, color='green')

    arw = math.floor(t / len(cities)) * len(cities)
    # arw = 0 # For pheremon graph
    for i in range(arw, t):
        if (i < len(x) - 1):
            plt.annotate('', xy=(x[i], y[i]), xycoords='data', xytext=(x[i + 1], y[i + 1]),
                         arrowprops={'arrowstyle': '<-'})

    # plt.plot(x,y, color='red')
    # plt.scatter(cx,cy, color = 'red')
    # Add labels to points
    for a, b in zip(x, y):
        label = f"({a},{b})"
        plt.annotate(label, (a, b))
    plt.xlim(0, 110)
    s = 'Particle: ' + str(math.floor(t / len(cities)))
    plt.title(s)


# This is for showing the current best path
def animate2(t):
    global current_fitness_index
    if (t < len(global_positions)):
        for i in range(len(cities)):
            x.append(global_positions[t][i][0])
            y.append(global_positions[t][i][1])
    plt.cla()
    plt.scatter(x, y, color='green')
    arw = math.floor(t / len(cities)) * len(cities)
    curr = arw / len(cities)
    if (global_fitness[int(curr)] < global_fitness[int(current_fitness_index)] or curr == 0):
        current_fitness_index = curr
    else:
        arw = 10 * current_fitness_index

    # for i in range(arw, t):
    if (arw < len(x) - 1):
        plt.plot(x[int(arw):int(arw + 10)], y[int(arw):int(arw + 10)], color='red')

    # Add labels to points
    for a, b in zip(x, y):
        label = f"({a},{b})"
        plt.annotate(label, (a, b))
    plt.xlim(0, 110)
    s = 'Current particle with best path: ' + str(int(current_fitness_index)) + ' with total distance of ' + str(global_fitness[int(current_fitness_index)])
    plt.title(s)


anim2 = matplotlib.animation.FuncAnimation(fig, animate, frames=10*pcount, init_func=lambda: None, interval=600)
anim = matplotlib.animation.FuncAnimation(fig, animate2, frames=10*pcount, init_func=lambda: None, interval=600)
anim.save('CurrentBest.gif', writer='pillow')
anim2.save('Iterations.gif', writer='pillow')
plt.show()
