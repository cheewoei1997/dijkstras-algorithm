# https://rosettacode.org/wiki/Dijkstra%27s_algorithm#Python
# ------------------------------------------------------------------------------
from collections import namedtuple, deque
from pprint import pprint as pp
import networkxApi as networkGraph

 
# ------------------------------------------------------------------------------
# Pretty self-explanatory
start_node = 'a'
dest_node = 'h'

# Specify the graph using the following format: (node1, node2, weight)
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
        pp(neighbours)
 
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
        pp(previous)
        s, u = deque(), dest
        while previous[u]:
            s.appendleft(u)
            u = previous[u]
        s.appendleft(u)
        return s


def drawGraph():
    networkGraph.addEdge(1, 2, 9)
    networkGraph.addEdge(1, 6, 14)
    networkGraph.addEdge(1, 7, 14)
    networkGraph.addEdge(2, 3, 23)
    networkGraph.addEdge(3, 4, 6)
    networkGraph.addEdge(3, 5, 2)
    networkGraph.addEdge(3, 6, 18)
    networkGraph.addEdge(3, 8, 19)
    networkGraph.addEdge(4, 5, 11)
    networkGraph.addEdge(4, 8, 6)
    networkGraph.addEdge(5, 6, 30)
    networkGraph.addEdge(5, 7, 20)
    networkGraph.addEdge(5, 8, 16)
    networkGraph.addEdge(6, 7, 5)
    networkGraph.addEdge(7, 8, 44)
    networkGraph.drawGraph()
    networkGraph.showGraph()


def main():
    graph = Graph(graphItem)
    pp(graph.dijkstra(start_node, dest_node))
    drawGraph()

if __name__ == "__main__":
    main()