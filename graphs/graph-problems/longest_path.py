# Finding the longest path  for a given graph as below

class Edge(object):
    def __init__(self, src=None, dest=None, weight=None):
        self.src = src
        self.dest = dest
        self.weight = weight


class Graph(object):
    def __init__(self, vertexCount=None, edges=[]):
        self.vertexCount = vertexCount
        self.edges = edges


def construct_graph():
    graph = Graph(6, [None] * 6)
    graph.edges = [[] for i in graph.edges]

    edge = Edge(0, 1, 5)
    graph.edges[edge.src].append(edge)

    edge = Edge(0, 2, 3)
    graph.edges[edge.src].append(edge)

    edge = Edge(1, 3, 6)
    graph.edges[edge.src].append(edge)

    edge = Edge(1, 2, 2)
    graph.edges[edge.src].append(edge)

    edge = Edge(2, 4, 4)
    graph.edges[edge.src].append(edge)

    edge = Edge(2, 5, 2)
    graph.edges[edge.src].append(edge)

    edge = Edge(2, 3, 7)
    graph.edges[edge.src].append(edge)

    edge = Edge(3, 5, 1)
    graph.edges[edge.src].append(edge)

    edge = Edge(3, 4, -1)
    graph.edges[edge.src].append(edge)

    edge = Edge(4, 5, -2)
    graph.edges[edge.src].append(edge)

    return graph


graph = construct_graph()
print(graph)
