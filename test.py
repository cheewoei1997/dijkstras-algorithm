# https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html#drawing-graphs
# ------------------------------------------------------------------------------
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
from math import sqrt


# # Creating a graph
# # Create an empty graph with no nodes and no edges.
# G = nx.Graph()

# # Add node(s), add_node(nodeName)
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# G.add_node(4)
# G.add_node(5)
# G.add_node(6)
# G.add_node(7)
# G.add_node(8)

# # Add edge(s), add_edge(node1, node2, key:value)
# G.add_edge(1, 2, weight=9)
# G.add_edge(1, 6, weight=14)
# G.add_edge(1, 7, weight=14)
# G.add_edge(2, 3, weight=23)
# G.add_edge(3, 4, weight=6)
# G.add_edge(3, 5, weight=2)
# G.add_edge(3, 6, weight=18)
# G.add_edge(3, 8, weight=19)
# G.add_edge(4, 5, weight=11)
# G.add_edge(4, 8, weight=6)
# G.add_edge(5, 6, weight=30)
# G.add_edge(5, 7, weight=20)
# G.add_edge(5, 8, weight=16)
# G.add_edge(6, 7, weight=5)
# G.add_edge(7, 8, weight=44)

# # Specify positioning of the graph using a dictionary
# # pos = graphviz_layout(G)
# pos = nx.spring_layout(G)

# # Draw out the graph
# nx.draw(G, pos, edge_color='black', width=1, linewidths=1, node_size=500, 
#     node_color='pink', labels={node:node for node in G.nodes()})

# # Keep nodes and edge labels in a dictionary
# edge_labels=dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])

# # Draw out the edge labels
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

# # Show the drawn graph
# plt.axis('off')
# plt.show()


# ------------------------------------------------------------------------------
# Creating a graph
# Create an empty graph with no nodes and no edges.
G = nx.Graph()

# Add node(s), add_node(nodeName)
def addNode(node=''):
    G.add_node(node)

# Add edge(s), add_edge(node1, node2, key:value)
def addEdge(node1='', node2='', val_weight=0):
    G.add_edge(node1, node2, weight=val_weight)

# Draw out the graph
def drawGraph():
    # Specify positioning of the graph using a dictionary
    pos=nx.spring_layout(G)

    # Keep nodes and edge labels in a dictionary
    edge_labels=dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])

    nx.draw(G, pos, edge_color='black', width=1,
        linewidths=1, node_size=500, node_color='pink',
        labels={node:node for node in G.nodes()})

    # Draw out the edge labels
    nx.draw_networkx_edge_labels(G, pos,
        edge_labels=edge_labels, font_color='black')


# Show the drawn graph
def showGraph():
    plt.axis('off')
    plt.show()