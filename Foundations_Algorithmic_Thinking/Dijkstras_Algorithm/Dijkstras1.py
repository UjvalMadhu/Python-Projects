# Project: Dijkstra's Algorithm for finding the shortest distance in a weighted graph
# The goal of this project is to find the shortest distance between two nodes A and C in a weighted graph, the graph is
# illustrated in the readme file.
# Acknowledgement: Robin Andrews, Compucademy, Foundations of Algorithmic Thinking with Python

# Author: Ujval Madhu
# C-Log: 1st Feb 2025
#==========================================================================================================================

import matplotlib.pyplot as plt
import heapq

# Defining the Required Graph
graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'D': 2, 'E': 2, 'C':5},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'D': 1, 'C': 5}
}

# Defining Node Positions for drawing the graph
node_positions = {
    'A': (0,2),
    'B': (2,2),
    'C': (4,1),
    'D': (0,0),
    'E': (2,0)
}

# Creating a figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,8))

# Drawing the edges and their weights
for start_node in graph:
    for end_node, weight in graph[start_node].items():
        start_pt = node_positions[start_node]
        end_pt   = node_positions[end_node]

        ax1.plot([start_pt[0], end_pt[0]],                 # x co-ordinates
                 [start_pt[1], end_pt[1]],                 # y co-ordinates
                 linestyle = "--",
                 linewidth = 3,
                 color ='black')   
        
        middle_x = (start_pt[0] + end_pt[0]) / 2
        middle_y = (start_pt[1]+ end_pt[1]) / 2

        ax1.text(middle_x, middle_y, str(weight),
                 fontsize = 20,
                 horizontalalignment = 'center',
                 verticalalignment   = 'center',
                 bbox = dict(facecolor = 'white', edgecolor = 'none', alpha = 0.7)
                )

# Drawing node circles with names
for node, pos in node_positions.items():
    ax1.plot(pos[0], pos[1], 'o', color = 'turquoise', markersize = 50)
    ax1.text(pos[0], pos[1], node, 
                    horizontalalignment = 'center',
                    verticalalignment   = 'center',
                    color = 'white',
                    fontsize = 20
            )

# Plot details
ax1.axis('equal')
ax1.margins(x = 0.2, y = 0.2)
#ax1.title("Weighted Graph Visualization", fontsize = 20, fontweight = 'bold')


# Creating a Function for Dijkstra's Algorithm

def dijkstrasDistCalc(i_graph, src):
    # Initialize the Calculated distance to all nodes from the source node
    dist        = {node: float('infinity') for node in i_graph}
    dist[src]   = 0

    # Create a Set to store visited nodes, sets are used as they have a faster lookup time and support only unique elements
    visited_nodes = set()

    # Create a Priority Queue to select minimum distance nodes
    pq = [(0,src)]                           # will prioritize based on 1st element i.e. distance

    while pq:

        selected_dist, selected_node = heapq.heappop(pq)              # gets the node with the minimum distance from pq

        if(selected_node) in visited_nodes:
            continue

        visited_nodes.add(selected_node)

        for neighbour, neighbour_edge in i_graph[selected_node].items():
            if neighbour not in visited_nodes:
                neighbour_dist = neighbour_edge + selected_dist

                if neighbour_dist < dist[neighbour]:
                    dist[neighbour] = neighbour_dist
                    heapq.heappush(pq, (neighbour_dist, neighbour))
    
    return dist



# Using Dijkstra's algorithm to find the shortest distance from Node A (Source) to Node C (Destination)

shortest_dist_from_A = dijkstrasDistCalc(graph, 'A')

# creating a table of all the shortest distances to nodes from A
table_data = [['Node', 'Shortest\nDistance\nfrom A']]
for node, shrtDist in shortest_dist_from_A.items():
    table_data.append([node, str(shrtDist)])

ax2.axis('off')
table = ax2.table(cellText = table_data, loc = 'center', cellLoc ='center', bbox = [0.1,0.2,0.8,0.6])

# Table Styling
table.auto_set_font_size(False)
table.set_fontsize(16)
table.scale(1.7,1.8)

for cell in table._cells:
    table._cells[cell].set_text_props(wrap=True)
    table._cells[cell].set_height(3)

# Adding Title to the plot
plt.suptitle("Graph Visualization and Shortest distances from Node A", fontsize = 25)

# Add captions below subplots
ax1.text(0.5, -0.1, 'Fig 1: Weighted Graph Structure', horizontalalignment='center', transform=ax1.transAxes, fontsize = 20)
ax2.text(0.5, -0.1, 'Fig 2: Shortest Path Distances', horizontalalignment='center', transform=ax2.transAxes, fontsize = 20)

# Plotting the Outputs
plt.show()