"""
Tests for Binary Tree
"""

from trees.trees import BinaryTree, Node, BinarySearchTree
import pytest


def test_bfs():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for A,B,C,D
    a_node = Node("A")
    b_node = Node("B")
    c_node = Node("C")
    d_node = Node("D")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["A", "B", "C", "D"]
    # set actual to return value of bfs call
    actual = tree.bfs()
    # assert actual is same as expected
    assert actual == expected
    print("test_bfs passed")


def test_bfs_2():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for A,B,C,D
    a_node = Node("1")
    b_node = Node("2")
    c_node = Node("3")
    d_node = Node("4")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["1", "2", "3", "4"]
    # set actual to return value of bfs call
    actual = tree.bfs()
    # assert actual is same as expected
    assert actual == expected
    print("test_bfs_2 passed")


def test_pre_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for 1,2,3,4
    a_node = Node("1")
    b_node = Node("2")
    c_node = Node("3")
    d_node = Node("4")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["1", "2", "4", "3"]
    # set actual to return value of pre_order call
    actual = tree.pre_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_pre_order_ passed")


def test_post_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for 1,2,3,4
    a_node = Node("1")
    b_node = Node("2")
    c_node = Node("3")
    d_node = Node("4")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["4", "2", "3", "1"]
    # set actual to return value of post_order call
    actual = tree.post_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_post_order_ passed")


def test_in_order():
    # Arrange
    # Create tree instance
    tree = BinaryTree()

    # Create Nodes for 1,2,3,4
    a_node = Node("1")
    b_node = Node("2")
    c_node = Node("3")
    d_node = Node("4")
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node

    # Add Root node to tree
    tree.root = a_node

    # set expected list
    expected = ["4", "2", "1", "3"]
    # set actual to return value of in_order call
    actual = tree.in_order()
    # assert actual is same as expected
    assert actual == expected
    print("test_in_order_ passed")


def test_empty_tree():
    # Create tree instance
    tree = BinarySearchTree()
    # Actual
    actual = tree.root
    # Expected
    expected = None
    # Assert
    assert actual == expected


def test_single_root_node():
    # Create tree instance
    tree = BinarySearchTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    # Actual
    actual = tree.root.value
    # Expected
    expected = 1
    # Assert
    assert actual == expected


def test_add_left_child_right_child():
    # Create tree instance
    tree = BinarySearchTree()
    tree.add(11)
    tree.add(2)
    tree.add(33)
    # Actual
    actual = (tree.root.left.value, tree.root.right.value)
    # Expected
    expected = (33, 2)
    # Assert
    assert actual == expected


def test_happy_path_max(max_tree):
    # Actual
    actual = max_tree.max_value()
    # Expected
    expected = 11
    # Assert
    assert actual == expected


def test_expected_failure_max(max_tree):
    # Actual
    actual = max_tree.max_value()
    # Expected
    expected = 9
    # Assert
    assert actual != expected


def test_edge_case_max(max_tree):
    max_tree.root = Node(20)
    # Actual
    actual = max_tree.max_value()
    # Expected
    expected = 20
    # Assert
    assert actual == expected


@pytest.fixture
def max_tree():
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    return tree
