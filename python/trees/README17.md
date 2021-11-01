# Challenge Summary

Write a function called breadth first

Arguments: tree

Return: list of all values in the tree, in the order they were encountered

## Whiteboard Process

![code17](python/trees/CodeChallenge17.png)

## Approach & Efficiency

Ceate function called breadth_first, then enqueue tree root, declare an empty list `list_of_items =[]`
check if the tree is empty it will return an empty list. Loop through the queue and check the left and right if they exist add them to the list, finally return the list.

Big O: O(n).

## Feature Tasks

[x] Write a function called breadth first

Arguments: tree

Return: list of all values in the tree, in the order they were encountered

## Unit Tests

[x] “Happy Path” - Expected outcome

[x] Expected failure

[x] Edge Case

## Pull Request

https://github.com/Faisal-Kushha/data-structures-and-algorithms/pull/34
