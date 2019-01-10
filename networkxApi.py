# https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html#drawing-graphs
# ------------------------------------------------------------------------------
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import numpy as np

# https://stackoverflow.com/questions/40632486/dot-exe-not-found-in-path-pydot-on-python-windows-7
# ------------------------------------------------------------------------------
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


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
    # pos = nx.spring_layout(G, scale=2, k=np.sqrt(len(G.nodes)))
    # https://networkx.github.io/documentation/stable/reference/drawing.html
    pos = nx.nx_pydot.graphviz_layout(G, prog='neato')

    # Keep nodes and edge labels in a dictionary
    edge_labels=dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])

    print(len(G.nodes))
    print(1/np.sqrt(len(G.nodes)))

    nx.draw(G, pos, edge_color='black', width=1, linewidths=1, node_size=500,
        node_color='pink', labels={node:node for node in G.nodes()})

    # Draw out the edge labels
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
        font_color='black')


# Show the drawn graph
def showGraph():
    plt.axis('off')
    plt.show()