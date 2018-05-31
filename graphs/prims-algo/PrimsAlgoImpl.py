# Implementation of Prims Algorithm

import sys


class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)
                       for rows in range(vertices)]]

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def primsMST(self):
        # To choose the minimum weight edge in cut
        key = [sys.maxsize] * self.vertices
        # Choose to  store the MST Details
        store_mst = [None] * self.vertices

        # make 0 index as the first key to proceed
        key[0] = 0
        # initial assign vertices visited set as False for all vertices
        min_set = [False] * self.vertices
        # for root node value set
        store_mst[0] = -1

        for cout in range(self.vertices):
            # find the min key acc to weight
            min_index = self.minkey(key, min_set)
            min_set[min_index] = True

            for v in range(self.vertices):
                if self.graph[min_index, v] > 0 and min_set[v] == False and key[v] > self.graph[min_index, v]:
                    key[v] = self.graph[min_index, v]
                    store_mst[v] = min_index
        self.printMST(store_mst)

    def minkey(self, key, min_set):

        min = sys.maxsize
        for v in range(self.vertices):
            if key[v] < min and min_set[v] == False:
                min = key[v]
                min_index = v
        return min_index


def construct_graph():
    graph = Graph(5)
    graph.graph = [[0, 2, 0, 6, 0],
                   [2, 0, 3, 8, 5],
                   [0, 3, 0, 0, 7],
                   [6, 8, 0, 0, 9],
                   [0, 5, 7, 9, 0],
                   ]
    return graph


if __name__ == '__main__':
    print(" :Implementation Prims Algorithms using Adjacency Matrix representation:")
    graph = construct_graph()
    graph.primsMST()
