from graphFunctions import Graph, namedtuple, drawGraph, swapNodes


# ------------------------------------------------------------------------------
# Pretty self-explanatory
# start_node = 'a'
# dest_node = 'h'

start_node = 'MLK'
dest_node = 'PHG'


# Specify the graph using the following format: (startNode, endNode, weight)
# graphItem = [('a', 'b', 9),  ('a', 'f', 14),  ('a', 'g', 14), ('b', 'c', 23),
#                ('c', 'f', 18), ('c', 'd', 6), ('c', 'h', 19), ('c', 'e', 2),
#                ('d', 'e', 11), ('d', 'h', 6), ('e', 'f', 30), ('e', 'g', 20),
#                ('e', 'h', 16), ('f', 'g', 5), ('g', 'h', 44)]

graphItem = [('JHR', 'MLK', 217),  ('MLK', 'NSN', 88), ('NSN', 'PJY', 59),
               ('PJY', 'KUL', 43), ('NSN', 'KUL', 70), ('JHR', 'PHG', 357),
               ('MLK', 'PHG', 396), ('KUL', 'PHG', 254), ('KUL', 'SGR', 27),
               ('PJY', 'SGR', 42), ('TRG', 'PHG', 226), ('TRG', 'KTN', 163),
               ('KTN', 'KDH', 354), ('KDH', 'PLS', 48), ('KUL', 'KTN', 436),
               ('KTN', 'PRK', 347), ('PRK', 'TRG', 365), ('KUL', 'PRK', 199),
               ('PRK', 'KDH', 239), ('PNG', 'KDH', 114), ('PNG', 'PRK', 157),
               ('PNG', 'KTN', 340), ('PNG', 'TRG', 442), ('PNG', 'KUL', 353),
               ('PNG', 'SGR', 360), ('PJY', 'PNG', 390)]


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