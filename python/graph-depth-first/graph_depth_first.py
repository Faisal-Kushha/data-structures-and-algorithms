from collections import deque


class Vertex:
    def __init__(self, value):
        self.value = value


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Stack:
    def __init__(self):
        self.dq = deque()

    def push(self, value):
        self.dq.append(value)

    def pop(self):
        self.dq.pop()


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        self.__adjacency_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def size(self):
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")
        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")
        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self.__adjacency_list.get(vertex, [])

    def depth_first(self, node):
        visited = []
        queue = Queue()
        queue.enqueue(node)
        visited.append(node)
        while queue:
            s = queue.dequeue()
            for x in graph.get_neighbors(s)[::-1]:
                if x not in visited:
                    visited.append(x)
                    queue.enqueue(x)
        return visited


if __name__ == '__main__':

    graph = Graph()

    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node('h')

    graph.add_edge(a, b)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, d)
    graph.add_edge(c, g)
    graph.add_edge(d, e)
    graph.add_edge(d, h)
    graph.add_edge(d, f)
    graph.add_edge(f, h)

    print(graph.depth_first(a)[8])
