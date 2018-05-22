# DFS implementation
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, s):
        visited = [False] * (len(self.graph))
        self.dfsUtil(s, visited)

    def dfsUtil(self, s, visited):
        visited[s] = True
        print(s, end=" ")
        for i in self.graph[s]:
            if visited[i] == False:
                self.dfsUtil(i, visited)


dfsGraph = Graph()
dfsGraph.addEdge(0, 1)
dfsGraph.addEdge(0, 2)
dfsGraph.addEdge(1, 2)
dfsGraph.addEdge(2, 0)
dfsGraph.addEdge(2, 3)
dfsGraph.addEdge(3, 3)

print(" ::: DFS Implementation using Adjacency list ::: ")
dfsGraph.dfs(2)
