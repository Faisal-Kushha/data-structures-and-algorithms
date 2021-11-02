from trees.tree_fizz_buzz import *

import pytest


def test_breadth_first(tree_test):
    expected = [1, 3, 5, 2, 4, 6, 11, 15]
    actual = tree_test.bfs()
    assert actual == expected


def test_empty_breadth_first():
    tree = k_ary_tree()
    tree = tree.bfs()
    expected = None
    actual = fizz_buzz_tree(tree)
    assert actual == expected


def test_fizz_buzz_tree(tree_test):
    tree = tree_test
    tree = tree.bfs()
    expected = ["1", "Fizz", "Buzz", "2", "4", "Fizz", "11", "FizzBuzz"]
    actual = fizz_buzz_tree(tree)
    assert actual == expected


@pytest.fixture
def tree_test():
    a = 1
    b = 3
    c = 5
    d = 2
    e = 4
    f = 6
    g = 11
    h = 15

    node_a = Node(a)
    node_c = Node(c)
    node_b = Node(b)
    node_d = Node(d)
    node_e = Node(e)
    node_f = Node(f)
    node_g = Node(g)
    node_h = Node(h)

    node_a.add_child(node_b)
    node_a.add_child(node_c)
    node_a.add_child(node_d)
    node_a.add_child(node_e)
    node_a.add_child(node_f)
    node_a.add_child(node_g)
    node_a.add_child(node_h)

    tree = k_ary_tree()
    tree.root = node_a

    return tree
