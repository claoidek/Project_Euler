# Reads the weighted network graph from external_files/107_network.txt and
# removes redundant edges to find the maximum saving in weight that can be
# achieved while still ensuring that the network is connected.

import time
import csv
from copy import deepcopy

# This conducts a depth-first search of the graph in order to ensure that each
# node is visited (i.e. the graph is connected).
def search_graph(visited, graph, starting_node):
    if starting_node not in visited:
        visited.add(starting_node)
        for neighbour in graph[starting_node]:
            search_graph(visited, graph, neighbour)

start = time.time()

num_nodes = 40
graph = {}
node_weights = {}

for node in range(1, num_nodes + 1):
    graph[node] = {}

with open("external_files/107_network.txt") as f:
    csv_file = csv.reader(f)
    node = 0
    for line in csv_file:
        node += 1
        connection = 0
        for entry in line:
            connection += 1
            if(entry != "-"):
                graph[node][connection] = int(entry)
                # As well as storing the weighted graph in a dictionary, we also
                # create a second dictionary (node_weights) so that we can find
                # the corresponding edges for each node weight easily. This will
                # allow us to iterate through the edges from heaviest to
                # lightest.
                if(node < connection):
                    if int(entry) not in node_weights:
                        node_weights[int(entry)] = [[node,connection]]
                    else:
                        node_weights[int(entry)].append([node,connection])

orig_weight = 0
for node in graph:
    for connection in graph[node]:
        orig_weight += graph[node][connection]
# Divide by two since we double count each weight
orig_weight //= 2

for node_weight in sorted(node_weights.items(), reverse = True):
    for connection in range(len(node_weight[1])):
        # Create a temporary copy of the graph with one edge removed.
        temp_graph = deepcopy(graph)
        temp_graph[node_weight[1][connection][0]].pop(node_weight[1][connection][1])
        temp_graph[node_weight[1][connection][1]].pop(node_weight[1][connection][0])
        visited = set()
        starting_node = next(iter(temp_graph))
        search_graph(visited,temp_graph,starting_node)
        if(len(visited) == num_nodes):
            # If the graph is still connected then we accept the new graph.
            graph = deepcopy(temp_graph)

minimal_weight = 0
for node in graph:
    for connection in graph[node]:
        minimal_weight += graph[node][connection]
# Divide by two since we double count each weight
minimal_weight //= 2
saving = orig_weight - minimal_weight

end = time.time()

print(saving)
print("Time taken: ", end-start, "s", sep="")
