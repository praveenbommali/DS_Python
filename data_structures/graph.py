# Defining the graph  template for re-use


class Edge:
    def __init__(self, src, dest, weight=None):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __hash__(self):
        return hash((self.src, self.dest))

    def __str__(self):
        return 'src:' + self.src.name + ', dest: ' + self.dest.name


class Vertex:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

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

    def add_edge(self, src, dest, weight=None):
        edge = Edge(src, dest, weight)
        self.edges.append(edge)

    def add_vertex(self, name):
        vertex = Vertex(name)
        self.vertices.append(vertex)
        return vertex

    def get_edges(self, src, dest):
        print(src, dest)
        for edge in self.edges:
            if edge.dest == dest and edge.src == src:
                print("edge btwn src", src, " -dest ", dest, " edge : ", edge)
                weight = edge.weight
                return weight


def construct_graph():
    graph = Graph()
    a = graph.add_vertex("a")
    b = graph.add_vertex("b")
    c = graph.add_vertex("c")
    d = graph.add_vertex("d")

    graph.add_edge(a, b, 3)
    graph.add_edge(b, c, 1)
    graph.add_edge(c, d, 2)
    graph.add_edge(d, b, 6)

    return graph


if __name__ == '__main__':
    print("basic Graph Template")
    graph = construct_graph()
    print(graph.get_edges("a", "b"))
