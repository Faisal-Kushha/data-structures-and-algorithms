from collections import deque


class Vertex:
    """
  Class for Adding a node to the graph
  Arguments: value
  Returns: The added node
  """

    def __init__(self, value):
        """
    Initalization for a Vertex to hold a value.

    """
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
        """
                The constructor method for the stack class and it initializes the dq property to a new double ended queue instance.
                """
        self.dq = deque()

    def push(self, value):
        """
                Store the passed value in a node and then push the node on top of the stack.

                PARAMETERS
                ----------
                        value: any
                                The value that will get stored in a node to be pushed on top of the stack.
                """
        self.dq.append(value)

    def pop(self):
        """
                Return the top node in a stack.
                """
        self.dq.pop()


class Edge:
    """
    a class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing

  """

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        """
    Initalization for a hashmap to hold the vertices
    """
        self.__adjacency_list = {}

    def add_node(self, value):
        """
      Method for Adding a node to the graph
      Arguments: value
      Returns: The added node
    """
        # new node
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def size(self):
        """ Returning the total number of nodes in the graph """
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
    Method to get all nodes in Graph
    Arguments: None
    return: All nodes
    """
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        """ Getting the collection of edges connected to a given node """
        return self.__adjacency_list.get(vertex, [])


def business_trip(graph, cities):
    x = True
    cost = 0
    for i in range(len(cities)-1):
        for city in graph.get_neighbors(cities[i]):
            z = city.weight
            if cities[i] == city.vertex:
                cost += z
            else:
                x = False
    return x, f'${cost}'


graph = Graph()
pandora = graph.add_node('pandora')
arendelle = graph.add_node('arendelle')
metroville = graph.add_node('metroville')
narnia = graph.add_node('narnia')
naboo = graph.add_node('naboo')
manstropolis = graph.add_node('manstropolis')
graph.add_edge(pandora, arendelle, 150)
graph.add_edge(pandora, metroville, 82)
graph.add_edge(arendelle, metroville, 99)
graph.add_edge(arendelle, manstropolis, 42)
graph.add_edge(metroville, manstropolis, 105)
graph.add_edge(metroville, naboo, 26)
graph.add_edge(metroville, narnia, 37)
graph.add_edge(narnia, naboo, 250)
graph.add_edge(manstropolis, naboo, 73)
cities = [metroville, pandora]
print(business_trip(graph, cities))
