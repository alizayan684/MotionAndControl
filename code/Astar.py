# ----------------------------------------------------------------------------
# Importing modules
# edges.csv file for V-REP kilobot motion planning scene.
# All lines beginning with a # are treated as a comment and ignored.
# Each line below is of the form
# ID1,ID2,cost
# where ID1 and ID2 are the IDs of the nodes connected by the edge and
# cost is the cost of traversing that edge (in either direction).
# -----------------------------------------------------------------------------
# nodes.csv file for V-REP kilobot motion planning scene.
# All lines beginning with a # are treated as a comment and ignored.
# Each line below has the form
# ID,x,y,heuristic-cost-to-go
# where ID is the unique integer ID number of the node (1 through N),
# (x,y) is the location of the node in the plane, and heuristic-cost-to-go
# is an optimistic estimate of the path length from that node to the
# goal node, as needed by A* search.
# -----------------------------------------------------------------------------

import csv
import math
from queue import PriorityQueue


# ------------------------------------------------------------------------------------------------------------------
class Node:
    def __init__(self, i_d, x, y, heuristic):
        self.id = i_d
        self.x = x
        self.y = y
        self.heuristic = heuristic
        self.parent = None
        self.g = math.inf
        self.f = math.inf

    def __lt__(self, other):
        # Comparing nodes by f value when they are added to the priority queue
        return self.f < other.f


# ------------------------------------------------------------------------------------------------------------------
# Defining a function to read nodes and edges from CSV files
def read_graph(nodes_file, edges_file):
    # Creating an empty list for nodes
    nodes = []
    with open(nodes_file) as nf:
        reader = csv.reader(nf)
        for row in reader:
            id = int(row[0])
            x = float(row[1])
            y = float(row[2])
            heuristic = float(row[3])
            node = Node(id, x, y, heuristic)
            nodes.append(node)

    # Creating an empty dictionary for the graph adjacency list
    graph = {}
    with open(edges_file) as ef:
        reader = csv.reader(ef)
        for row in reader:
            id1 = int(row[0])
            id2 = int(row[1])
            cost = float(row[2])
            if id1 not in graph:
                graph[id1] = []
            graph[id1].append((id2, cost))
            if id2 not in graph:
                graph[id2] = []
            graph[id2].append((id1, cost))

    return nodes, graph


# ------------------------------------------------------------------------------------------------------------------
# Defining a function to get the neighboring nodes for a given node
def get_neighbors(node, nodes, graph):
    neighbors = []
    if node.id in graph:
        for edge in graph[node.id]:
            neighbor_id = edge[0]
            neighbor_cost = edge[1]
            for n in nodes:
                if n.id == neighbor_id:
                    neighbors.append((n, neighbor_cost))
                    break

    return neighbors


# ------------------------------------------------------------------------------------------------------------------
# Defining a function to implement the A* algorithm
def a_star(start, goal, nodes, graph):
    path = []
    if goal == start:
        path.append(start)
        return path
    open_set = PriorityQueue()
    closed_set = set()
    start_node = None
    goal_node = None
    for node in nodes:
        if node.id == start:
            start_node = node
        if node.id == goal:
            goal_node = node
    # Checking if the start and goal nodes are valid
    if start_node is None or goal_node is None:
        return None
    # Initializing the g and f values of the start node
    start_node.g = 0
    start_node.f = start_node.g + start_node.heuristic
    # Adding the start node to the open set
    open_set.put(start_node)
    # Creating an empty set for the closed set
    # Looping until the open set is empty
    while not open_set.empty():
        current = open_set.get()
        closed_set.add(current)
        if current == goal_node:
            while current is not None:
                path.append(current.id)
                current = current.parent
            path.reverse()
            return path
        neighbors = get_neighbors(current, nodes, graph)
        for neighbor in neighbors:
            neighbor_node = neighbor[0]
            neighbor_cost = neighbor[1]
            if neighbor_node in closed_set:
                continue
            if neighbor_node.g > current.g + neighbor_cost:
                neighbor_node.g = current.g + neighbor_cost
                neighbor_node.f = neighbor_node.g + neighbor_node.heuristic
                neighbor_node.parent = current
                if neighbor_node not in open_set.queue:
                    open_set.put(neighbor_node)
    return None


# ------------------------------------------------------------------------------------------------------------------
# Defining a function to write the optimal path to a CSV file
def write_path(output_path, output_file_path):
    # Checking if the path is valid
    if output_path is None:
        print("No path exists.")
        return
        # Opening the output file
    with open(output_file_path, "w") as of:
        # Creating a CSV writer object
        writer = csv.writer(of)
        # Looping through each node id in the path
        writer.writerow(output_path)
        # Calling the functions with appropriate arguments and testing your code


# ------------------------------------------------------------------------------------------------------------------
# Reading nodes and edges from CSV files (change file names as needed)
nodes, graph = read_graph("Scene5_example/nodes.csv", "Scene5_example/edges.csv")
# Implementing A* algorithm to find optimal path from start to goal (change ids as needed)
start = 1  # Start node id
goal = 12  # Goal node id
path = a_star(start, goal, nodes, graph)
# Writing optimal path to CSV file (change file name as needed)
output_file = "path.csv"
write_path(path, output_file)

# End of code
# ------------------------------------------------------------------------------------------------------------------
