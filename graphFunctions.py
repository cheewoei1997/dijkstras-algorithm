# https://rosettacode.org/wiki/Dijkstra%27s_algorithm#Python
# ------------------------------------------------------------------------------
from collections import namedtuple, deque
from pprint import pprint as pp
import matplotlib.pyplot as plt
import numpy as np

# https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html#drawing-graphs
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout

# https://stackoverflow.com/questions/40632486/dot-exe-not-found-in-path-pydot-on-python-windows-7
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# ------------------------------------------------------------------------------
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


class Graph():
    def __init__(self, edges):
        self.edges = edges2 = [Edge(*edge) for edge in edges]
        self.vertices = set(sum(([e.start, e.end] for e in edges2), []))
 
    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))
        print('NEIGHBOURS')
        # pp(neighbours)
 
        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:                           # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        print('\nSMALLEST VALUE')
        # pp(previous)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s


def drawGraph(graphItem, totalNodes, path, startNode, endNode, weight):
    # Creating a graph
    # Create an empty graph with no nodes and no edges.
    G = nx.DiGraph()

    # Path chosen by Dijkstra's Algorithm
    pStartNode = []
    pEndNode = []
    pWeights = []

    # Generate start nodes and end nodes in two separate lists
    for idx, val in enumerate(path):
        pEndNode.append(val)
        pStartNode.append(val)
        if idx == 0:
            pEndNode.pop()
    pStartNode.pop()

    # Combine the two seperate lists into one
    pathEdges = list(zip(pStartNode, pEndNode))

    # Obtain the weight of each step in the path
    pWeights = [pWeights.append(item[2]) for item in graphItem for pathEdge
        in pathEdges if (pathEdge[0] == item[0] and pathEdge[1] == item[1])]
    blackEdges = [edge for edge in G.edges() if edge not in pathEdges]

    # Add edges or nodes into the graph
    for i in range(totalNodes):
        G.add_edge(startNode[i], endNode[i], weight=weight[i])

    # Keep nodes and edge labels in a dictionary
    edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])

    # Specify positioning of the graph using a dictionary
    # https://networkx.github.io/documentation/stable/reference/drawing.html
    pos = nx.nx_pydot.graphviz_layout(G, prog='neato')

    nx.draw(G, pos, edge_color='black', width=1, linewidths=1, node_size=500,
        node_color='pink', labels={node:node for node in G.nodes()}, arrows=False)

    # Draw out the edge labels
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
        font_color='black')

    nx.draw_networkx_edges(G, pos, edgelist=pathEdges, edge_color='red',
        arrows=True, arrowsize=24)
    nx.draw_networkx_edges(G, pos, edgelist=blackEdges, arrows=False)
    
    showGraph()


# Show the drawn graph
def showGraph():
    plt.axis('off')
    plt.show()