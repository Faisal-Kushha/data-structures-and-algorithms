import pytest

from graph import *


def test_add_node():
    graph = Graph()
    expected = "test"
    actual = graph.add_node('test').value
    assert actual == expected


def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_node('spam')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_get_nodes():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    loner = Vertex('loner')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node('banana')

    apple = graph.add_node('apple')

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == 'banana'

    assert neighbor_edge.weight == 44


def test_happy_path():
    graph = Graph()
    one = graph.add_node('one')
    two = graph.add_node('two')
    three = graph.add_node('three')
    graph.add_edge(one, two)
    graph.add_edge(two, one)
    graph.add_edge(one, three)
    graph.add_edge(two, three)
    graph.add_edge(three, one)
    graph.add_edge(three, two)
    actual = graph.breadth_first_search(three)
    print(actual)
    expected = ['one', 'two', 'three']
    assert actual == expected


def test_edge_case():
    graph = Graph()
    one = Vertex('one')
    actual = graph.breadth_first_search(one)
    expected = 'This vertex is not in the graph'
    assert actual == expected


def test_expected_failure():
    graph = Graph()
    one = graph.add_node('one')
    two = graph.add_node('two')
    three = graph.add_node('three')
    graph.add_edge(one, two)
    graph.add_edge(two, one)
    graph.add_edge(two, three)
    graph.add_edge(two, three)
    graph.add_edge(three, two)
    actual = graph.breadth_first_search(one)
    expected = ['one', 'two', 'three']
    assert actual != expected
