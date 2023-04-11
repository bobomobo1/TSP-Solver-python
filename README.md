# TSP-Solver-python
An implementation of Particle Swarm Optimization on the Traveling Salesman Problem. This was done as an assignment for COIS-4550.

* Produces a random set of points on a graph (0,100)
* Uses a PSO(Partical Swarm Optimization) algorithm to caluculate the quickest route
* Generates matplotlib animations to visualize the algorithm

### Iteration Animation
<p align="center">
    <img src="Iterations.gif" alt="Current iteration" title="Iteration Animation" width="300" height="300">   
</p>

### Current Best Route Animation
<p align="center">
 <img src="CurrentBest.gif" alt="Current best route" title="Current Best Route Animation" width="300" height="300">
 </p>

 ### Coordinates of Best Route
<p align="center">
 <img src="Results.png" alt="Bst route" title="Best Route">
 </p>

## Swarm Intelligence

Swarm intelligence is an AI technique developed from studying real life occurrences. It is easy to about the general idea of swarm intelligence when it is related to an a school of fish. The school of fish has many individuals, isn't under control, but is self-organized as a whole. 

Key characteristics of swarm intelligence:
* Has many individuals
* Doesn't have a controler - decentralized
* Usually consists of 1 type of individual
* Individuals interact with each other and the environment
* Those interactions are what creates a self-organizing system which forms the results

Unique possibilities arise due to the techniques property of forming organized results, while not having a controller. It is a group of simple individuals, that become intelligent as a group. Also, even if a subgroup of individuals fail, the likelyhood of still getting results are still high(robust). 

Disadvantages:
* Sensitive - minor rule change can change alter the entire group
* Hard to predict group results from the individual level
* Difficult to implement and understand

Swarm intelligence has some notable algorithms:
* Ant colony optimization - find best path when moving through routes, record strong positions to simulate pheromones that other ants will migrate to
* Particle swarm optimization - particles move through space, keeping track of its location, the particles best value is stored (fitness value), the best amongst the particles is also stored. Particles change velocity each iteration to head to the best fitness locations.

### Applications
The applications of swarm intelligence include:
* Cargo routing
* Production scheduling 
* Crowd simulation
* Clustering

The future of self-driving will use swarm intelligence. Imagine the cars as the individuals. Seeing traffic and interacting with the environment. This can be shared to other cars creating one big group of traffic data that can be utilized to improve every ones driving. 





