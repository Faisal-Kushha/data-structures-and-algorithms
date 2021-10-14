from linked_list.linked_list import Node, LinkedList
import pytest


def test_import():
    assert LinkedList


def test_node_has_int_data():
    expected = 1
    node = Node(1)
    actual = node.value
    assert actual == expected


def test_node_has_str_data():
    expected = "x"
    node = Node("x")
    actual = node.value
    assert actual == expected


def test_node_is_a_Node():
    expected = "Node"
    node = Node(1)
    actual = type(node).__name__
    assert actual == expected


def test_node_without_value():
    with pytest.raises(TypeError):
        node = Node()


def test_new_linked_list_is_empty():
    expected = None
    x = LinkedList()
    actual = x.head
    assert actual == expected


def test_linked_list_insert():
    expected = None
    x = LinkedList()
    actual = x.insert(1)
    assert actual == expected


def test_linked_list_includes_true():
    expected = True
    LinkedList().insert(1)
    LinkedList().insert(2)
    LinkedList().insert(3)
    actual = LinkedList().includes(1)
    assert actual == expected


def test_linked_list_includes_false():
    expected = False
    LinkedList().insert(1)
    LinkedList().insert(2)
    LinkedList().insert(3)
    actual = LinkedList().includes(4)
    assert actual == expected


def test_return_all_values():
    expected = '( 1 ) -> ( 2 ) -> ( 3 ) -> NULL'
    x = LinkedList()
    actual = x.__str__()
    assert actual == expected
