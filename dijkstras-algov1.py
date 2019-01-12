from graphFunctions import Graph, namedtuple, drawGraph


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
 
def main():
    graph = Graph(graphItem)
    path = graph.dijkstra(start_node, dest_node)

    totalNodes = len(graphItem)
    startNode = [item[0] for item in graphItem]
    endNode = [item[1] for item in graphItem]
    weight = [item[2] for item in graphItem]

    drawGraph(graphItem, totalNodes, path, startNode, endNode, weight)


if __name__ == "__main__":
    main()