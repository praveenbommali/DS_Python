# Implementation of Topological Sorting  algorithm
# Adopted DFS Algorithm


from collections import defaultdict


class Graph(object):
    def __init__(self, vertex_count):
        self.adjlist_graph = defaultdict(list)
        self.vertex_count = vertex_count

    def add_edge(self, src, dest):
        self.adjlist_graph[src].append(dest)

    def topology_sort(self):
        visited = [False] * self.vertex_count
        stack = []

        for i in range(self.vertex_count):
            if not visited[i]:
                print("index :: ", self.adjlist_graph[i])
                self.topology_util(i, visited, stack)

        print(stack)

    def topology_util(self, index, visited, stack):
        visited[index] = True

        for i in self.adjlist_graph[index]:
            if visited[i] == False:
                self.topology_util(i, visited, stack)

        stack.insert(0, index)


def construct_graph():
    graph = Graph(vertex_count)
    graph.add_edge(5, 2)
    graph.add_edge(5, 0)
    graph.add_edge(4, 0)
    graph.add_edge(4, 1)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)

    return graph


if __name__ == '__main__':
    vertex_count = 6
    graph = construct_graph()
    graph.topology_sort()
