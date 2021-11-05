# Code Challenge: Class 15: Binary Tree and BST Implementation

## Challenge

### Node

[x] Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

### Binary Tree

[x] Create a Binary Tree class

[x] Define a method for each of the depth first traversals:
pre order
in order
post order which returns an array of the values, ordered appropriately.

[x] Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

### Binary Search Tree

[x] Create a Binary Search Tree class

This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:

[x] Add

Arguments: value

Return: nothing

Adds a new node with that value in the correct location in the binary search tree.

[x] Contains

Argument: value

Returns: boolean indicating whether or not the value is in the tree at least once.

## Structure and Testing

Write tests to prove the following functionality:

[x] Can successfully instantiate an empty tree

[x] Can successfully instantiate a tree with a single root node

[x] Can successfully add a left child and right child to a single root node

[x] Can successfully return a collection from a preorder traversal

[x] Can successfully return a collection from an inorder traversal

[x] Can successfully return a collection from a postorder traversal

## Approach & Efficiency

I created a 'Node' class that has properties for the value stored in the node for both side the left and the right. Then I created a 'Binary Tree class' thet had a methods for each of the depth first traversals: pre order, in order, post order. Additionally I created a 'Binary Search Tree class' which had two methods: 'Add' method that going to add a new node with value in certain location in the binary search tree, and 'Contains' method that will return True or False if the value is in the tree or not. MoreOver, I created a tests for esch methods. Big O: O(1), O(n).

## API

```
Breadth First
A binary tree method which returns a list of items that it take input as None and return tree items
```

```
Pre Order
A binary tree method which returns a list of items in pre order and it will take input as None and return tree items.
sub method : walk () to make the recursion staff
```

```
In Order
A binary tree method which returns a list of items in order and it will take input as None and return tree items.
sub method : walk () to make the recursion staff
```

```
Post Order
A binary tree method which returns a list of items in post order and it will take input as None and return tree items.
sub method : walk () to make the recursion staff
```

```
Binary Search Tree class and it's a sub-class of the Binary Tree Class, it has two methods:
1- Add Method which take:-
Arguments: value
Return: nothing

2- Contains Method which take:-
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.
```

## Pull Request

https://github.com/Faisal-Kushha/data-structures-and-algorithms/pull/32
