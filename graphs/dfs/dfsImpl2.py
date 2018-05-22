# DFS Implementation


class Graph(object):
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_list = [[] for i in range(vertex_count)]

    def add_edge(self, src, dst):
        self.adj_list[src].append(dst)

    def dfsutil(self, srtV, visited):
        visited[srtV] = 1
        print(srtV, end=" ")

        for vertex in self.adj_list[srtV]:
            if not visited[vertex]:
                self.dfsutil(vertex, visited)

    def dfs(self, srtV):
        visited = [0] * graph.vertex_count
        self.dfsutil(srtV, visited)


def costruct_graph():
    graph = Graph(4)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    return graph


if __name__ == '__main__':
    graph = costruct_graph()
    graph.dfs(2)
