import pytest
from tree_intersection import *


def test_happy_path(prepared_tree1, prepared_tree2):

    actual = tree_intersection(prepared_tree1, prepared_tree2)
    expected = [100, 160, 125, 175, 200, 350, 500]
    assert actual == expected


def test_edge_case():
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    actual = tree_intersection(tree1, tree2)
    expected = 'Tree is empty'

    assert actual == expected


def test_expected_failure(prepared_tree1, prepared_tree2):
    prepared_tree1.root.left = Node_tree(600)
    actual = tree_intersection(prepared_tree1, prepared_tree2)
    expected = [100, 160, 125, 175, 200, 350, 500]
    assert actual != expected


@pytest.fixture
def prepared_tree1():
    tree1 = BinaryTree()
    tree1.root = Node_tree(150)
    tree1.root.left = Node_tree(100)
    tree1.root.right = Node_tree(250)
    tree1.root.left.left = Node_tree(75)
    tree1.root.left.right = Node_tree(160)
    tree1.root.right.left = Node_tree(200)
    tree1.root.right.right = Node_tree(350)
    tree1.root.left.right.left = Node_tree(125)
    tree1.root.left.right.right = Node_tree(175)
    tree1.root.right.right.left = Node_tree(300)
    tree1.root.right.right.right = Node_tree(500)
    return tree1


@pytest.fixture
def prepared_tree2():
    tree2 = BinaryTree()
    tree2.root = Node_tree(42)
    tree2.root.left = Node_tree(100)
    tree2.root.right = Node_tree(600)
    tree2.root.left.left = Node_tree(15)
    tree2.root.left.right = Node_tree(160)
    tree2.root.right.left = Node_tree(200)
    tree2.root.right.right = Node_tree(350)
    tree2.root.left.right.left = Node_tree(125)
    tree2.root.left.right.right = Node_tree(175)
    tree2.root.right.right.left = Node_tree(4)
    tree2.root.right.right.right = Node_tree(500)
    return tree2
