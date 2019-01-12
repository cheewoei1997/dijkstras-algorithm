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
# Pretty self-explanatory
start_node = 'a'
dest_node = 'h'

# Specify the graph using the following format: (startNode, endNode, weight)
graphItem = [('a', 'b', 9),  ('a', 'f', 14),  ('a', 'g', 14), ('b', 'c', 23),
               ('c', 'f', 18), ('c', 'd', 6), ('c', 'h', 19), ('c', 'e', 2),
               ('d', 'e', 11), ('d', 'h', 6), ('e', 'f', 30), ('e', 'g', 20),
               ('e', 'h', 16), ('f', 'g', 5), ('g', 'h', 44)]


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
                if alt < dist[v]:                                  # Relax (u,v,a)
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


def drawGraph(totalNodes, startNode, endNode, weight):
    # Creating a graph
    # Create an empty graph with no nodes and no edges.
    G = nx.Graph()
    
    # Add edges or nodes into the graph
    for i in range(totalNodes):
        G.add_edge(startNode[i], endNode[i], weight=weight[i])

    # Specify positioning of the graph using a dictionary
    # pos = nx.spring_layout(G, scale=2, k=np.sqrt(len(G.nodes)))
    # https://networkx.github.io/documentation/stable/reference/drawing.html
    pos = nx.nx_pydot.graphviz_layout(G, prog='neato')

    # Keep nodes and edge labels in a dictionary
    edge_labels = dict([((u, v,), d['weight']) for u, v, d in G.edges(data=True)])

    nx.draw(G, pos, edge_color='black', width=1, linewidths=1, node_size=500,
        node_color='pink', labels={node:node for node in G.nodes()})

    # Draw out the edge labels
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,
        font_color='black')

    showGraph()


# Show the drawn graph
def showGraph():
    plt.axis('off')
    plt.show()


def main():
    graph = Graph(graphItem)
    # pp(graph.dijkstra(start_node, dest_node))
    path = graph.dijkstra(start_node, dest_node)

    totalNodes = len(graphItem)
    startNode = [item[0] for item in graphItem]
    endNode = [item[1] for item in graphItem]
    weight = [item[2] for item in graphItem]

    drawGraph(totalNodes, startNode, endNode, weight)


if __name__ == "__main__":
    main()