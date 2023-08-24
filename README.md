# A* Algorithm Implementation and Simulation

This project implements the A* algorithm for finding the shortest path between two nodes in a graph. The algorithm is written in python and uses the nodes and edges files as input. The output is a path file containing the optimal path's node IDs. The project also simulates the path on CoppeliaSim, a robotics simulation software, using the 4 files above.

## Requirements

- Python 3.8 or higher
- CoppeliaSim 4.2 or higher

## Usage
This is a part of the Robot Motion Planning and Control course at Northwestern University on Coursera.


## Input Files

The input files have the following format:

- **nodes.csv**: A comma-separated file that contains information about each node in the graph. Each row represents a node and has three columns: `id`, `x`, and `y`. The `id` column is a unique integer identifier for each node. The `x` and `y` columns are the coordinates of each node in meters.
- **edges.csv**: A comma-separated file that contains information about each edge in the graph. Each row represents an edge with three columns: `start`, `end`, and `cost`. The `start` and `end` columns are the IDs of the nodes that are connected by the edge. The `cost` column is a positive float value that represents the distance between the nodes in meters.
- **obstacles.csv**: A comma-separated file that contains information about each obstacle in the simulation. Each row represents an obstacle and has four columns: `id`, `x`, `y`, and `radius`. The `id` column is a unique integer identifier for each obstacle. The `x` and `y` columns are the coordinates of the center of each obstacle in meters. The `radius` column is a positive float value that represents the radius of each obstacle in meters.

## Output File

The output file has the following format:

- **path.csv**: A comma-separated file that contains information about the optimal path found by the algorithm. Each column represents a node in the path and has one column: `id`. The `id` column is the ID of each node in the path. The order of columns indicates the order of nodes in the path from start to goal.

here is a screenshot of the simulation results:
![Sim](https://github.com/alizayan684/MotionAndControl/blob/main/Screenshot%202023-08-15%20023655.png).
