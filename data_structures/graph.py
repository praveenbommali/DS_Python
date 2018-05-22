# Defining the graph  template for re-use


class Edge:
    def __init__(self, src, dest, weight=None):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __str__(self):
        return 'src:'+self.src.name + ', dest: '+self.dest.name


class Vertex:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name




class AbstractGraph:
    def add_edge(self, src, dest, weight=None, directed=True):
        raise NotImplementedError

    def create_vertex(self, name):
        raise NotImplementedError

    def get_weight(self, src, dest):
        raise NotImplementedError

    def get_edges(self, src):
        raise NotImplementedError


class Graph(AbstractGraph):
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_edge(self,src,dest,weight=None):
        edge = Edge(src,dest,weight)
        self.edges.append(edge)

    def add_vertex(self,name):
        vertex = Vertex(name)
        self.vertices.append(vertex)
        return vertex

    


def construct_graph():
    pass


if __name__ == '__main__':
    pass
