# BFS implementation


import queue


class Graph(object):
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_list = [[] for i in range(vertex_count)]

    def add_edge(self, src, dst):
        self.adj_list[src].append(dst)

    def bfs(self, srtV):
        visited = [False] * graph.vertex_count
        q_data = queue.Queue()
        q_data.put(srtV)
        visited[srtV] = 1
        print(srtV, end=" ")

        while not q_data.empty():
            adj_node = q_data.get()

            for vertex in self.adj_list[adj_node]:
                if not visited[vertex]:
                    print(vertex, end=" ")
                    visited[vertex] = 1
                    q_data.put(vertex)


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
    print("BFS Implementation using standard approach")
    graph = costruct_graph()
    graph.bfs(2)
