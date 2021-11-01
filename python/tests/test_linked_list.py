from linked_list.linked_list import Node, LinkedList
import pytest


def test_import():
    assert LinkedList


def test_node_has_int_data():
    # Arrange
    expected = 1
    # Actual
    node = Node(1)
    actual = node.value
    # Assert
    assert actual == expected


def test_node_has_str_data():
    # Arrange
    expected = "x"
    # Actual
    node = Node("x")
    actual = node.value
    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange
    expected = "Node"
    # Actual
    node = Node(1)
    actual = type(node).__name__
    # Assert
    assert actual == expected


def test_node_without_value():

    with pytest.raises(TypeError):
        node = Node()


def test_new_linked_list_is_empty():
    # Arrange
    expected = None
    # Actual
    ll = LinkedList()
    actual = ll.head
    # Assert
    assert actual == expected


def test_linked_list_insert():
    # Arrange
    expected = None
    # Actual
    ll = LinkedList()
    actual = ll.insert(1)
    # Assert
    assert actual == expected


def test_linked_list_includes_true():
    # Arrange
    expected = True
    # Actual
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    actual = ll.includes(1)
    # Assert
    assert actual == expected


def test_linked_list_includes_false():
    # Arrange
    expected = False
    # Actual
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    actual = ll.includes(4)
    # Assert
    assert actual == expected


def test_return_all_values():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 3 } -> NULL'
    # Actual
    ll = LinkedList()
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    actual = ll.__str__()
    assert actual == expected


def test_add_node():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 3 } -> NULL'
    # Actual
    ll = LinkedList()
    ll.append(3)
    ll.insert(2)
    ll.insert(1)

    actual = ll.__str__()
    print(actual)
    # Assert
    assert actual == expected


def test_add_multiple_nodes():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 7 } -> { 9 } -> { 11 } -> NULL'
    # Actual
    ll = LinkedList()
    ll.append(9)
    ll.append(11)
    ll.insert(7)
    ll.insert(2)
    ll.insert(1)
    actual = ll.__str__()

    # Assert
    assert actual == expected


def test_insert_node_before_middle():
    # Arrange
    expected = '{ 1 } -> { 4 } -> { 2 } -> { 3 } -> NULL'
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_before(2, 4)
    actual = ll.__str__()

    # Assert
    assert actual == expected


def test_insert_node_before_head():
    # Arrange
    expected = '{ 4 } -> { 3 } -> { 2 } -> { 1 } -> NULL'
    # Actual
    ll = LinkedList()
    ll.append(4)
    ll.append(3)
    ll.append(1)
    ll.insert_before(1, 2)
    actual = ll.__str__()

    # Assert
    assert actual == expected


def test_insert_node_after_middle():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> NULL'
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.insert_after(2, 3)
    actual = ll.__str__()
    print(actual)
    # Assert
    assert actual == expected


def test_insert_node_after_end():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> NULL'
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insert_after(3, 4)
    actual = ll.__str__()
    print(actual)
    # Assert
    assert actual == expected


def test_kth_happy():
    # Arrange
    expected = 6
    # Actual
    ll = LinkedList()
    ll.append(4)
    ll.append(5)
    ll.append(6)
    actual = ll.kth(2)
    print(actual)
    # Assert
    assert actual == expected


def test_kth_greater():
    # Arrange
    expected = "k value is greater than the length of the linked list"
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.kth(7)
    print(actual)
    # Assert
    assert actual == expected


def test_kth_negative():
    # Arrange
    expected = "k value is not a positive integer"
    # Actual
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.kth(-3)
    print(actual)
    # Assert
    assert actual == expected


def test_kth_size_one():
    # Arrange
    expected = 1
    # Actual
    ll = LinkedList()
    ll.append(1)
    actual = ll.kth(0)
    print(actual)
    # Assert
    assert actual == expected


def test_kth_middle():
    # Arrange
    expected = 5
    # Actual
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(6)
    ll.append(7)
    ll.insert_before(6, 5)
    actual = ll.kth(2)
    print(actual)
    # Assert
    assert actual == expected


def test_kth_same_length():
    # Arrange
    expected = "k value and the length of the list are the same"
    # Actual
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(6)
    ll.append(7)
    actual = ll.kth(4)
    print(actual)
    # Assert
    assert actual == expected


def test_zip():
    # Arrange
    expected = '{ 1 } -> { 2 } -> { 3 } -> { 4 } -> { 5 } -> { 6 } -> NULL'
    # Actual
    ll_one = LinkedList()
    ll_two = LinkedList()
    ll_one.insert(5)
    ll_one.insert(3)
    ll_one.insert(1)
    ll_two.insert(6)
    ll_two.insert(4)
    ll_two.insert(2)
    ll_one.zip(a=ll_one, b=ll_two)
    actual = ll_one.__str__()
    print(actual)
    # Assert
    assert actual == expected
