# Challenge Summary

Write the following method for the Binary Tree class that find the maximum value.

Arguments: none

Returns: number

Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process

![code16](python/trees/CodeChallenge16.png)

## Approach & Efficiency

Ceate a method called max_value and declare a variable for the maximum value = 0, Use the walk function that take a node as an argument then it'll check if there is a left node and check if there is a right node, within every check the walk function will be called again to check if the node value more than the maximum value, at the end it will check if the root value is greater than maximum value.

Big O: O(n), O(1).

## Solution

```
Input = tree
Output = 11

self.max=0
walk(Node(2))

if Node(7): True
   walk(Node(7))

if Node(5): True
   walk(Node(5))

if 2>11: False

return 11
```

## Feature Tasks

[x] Write the following method for the Binary Tree class, find maximum value

Arguments: none

Returns: number

Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Unit Tests

[x] “Happy Path” - Expected outcome

[x] Expected failure

[x] Edge Case

## Pull Request

https://github.com/Faisal-Kushha/data-structures-and-algorithms/pull/33
