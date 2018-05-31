# Implementation of Union and Find
# By using we can find the Graph forming cycles or not

from collections import defaultdict


class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def isCyclic(self):

        parent = [-1] * (self.vertices)

        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                print(x, " ", y)
                if x == y:
                    return True
                self.union(parent, x, y)

    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    def union(self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set


def construct_graph():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    return graph


if __name__ == '__main__':
    graph = construct_graph()
    print("Graph is Cyclic ? ", graph.isCyclic())
