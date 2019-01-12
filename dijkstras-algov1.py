from graphFunctions import Graph, namedtuple, drawGraph, swapNodes


# ------------------------------------------------------------------------------
# Pretty self-explanatory
start_node = 'a'
dest_node = 'h'

# start_node = 'KED'
# dest_node = 'KTN'


# Specify the graph using the following format: (startNode, endNode, weight)
graphItem = [('a', 'b', 9),  ('a', 'f', 14),  ('a', 'g', 14), ('b', 'c', 23),
               ('c', 'f', 18), ('c', 'd', 6), ('c', 'h', 19), ('c', 'e', 2),
               ('d', 'e', 11), ('d', 'h', 6), ('e', 'f', 30), ('e', 'g', 20),
               ('e', 'h', 16), ('f', 'g', 5), ('g', 'h', 44)]

# graphItem = [('MLK', 'KUL', 109),  ('KUL', 'KTN', 250), ('MLK', 'JHB', 300),
#                ('KUL', 'PNG', 500), ('KUL', 'KED', 154), ('KED', 'PNG', 347),
#                ('KTN', 'TRG', 300), ('TRG', 'KLN', 231), ('KED', 'PER', 87),
#                ('JHB', 'SG', 210)]


# ------------------------------------------------------------------------------
 
def main():
    totalNodes = len(graphItem) * 2
    startNode = [item[0] for item in graphItem]
    endNode = [item[1] for item in graphItem]
    weight = [item[2] for item in graphItem]

    extendedNodes = swapNodes(startNode, endNode, weight)
    newGraphItem = list(zip(extendedNodes[0], extendedNodes[1], extendedNodes[2]))

    newStartNode = extendedNodes[0]
    newEndNode = extendedNodes[1]
    newWeight = extendedNodes[2]

    graph = Graph(newGraphItem)
    path = graph.dijkstra(start_node, dest_node)
    print('Shortest path:', path)

    drawGraph(newGraphItem, totalNodes, path, newStartNode, newEndNode, newWeight)


if __name__ == "__main__":
    main()