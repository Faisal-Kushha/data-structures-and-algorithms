# Challenge Summary

Write a function called tree_intersection that takes two binary trees as parameters.

Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.

## Whiteboard Process

<!-- Embedded whiteboard image -->

## Approach & Efficiency

Create a function that takes 2 tree as input then declare an empty arr, after that check if the tree is empty, create walk function that take node as input and check if the hashtable contains the node.value than add the value to the array, if not add the value to the hashtable. Check if there is node.left then check if there is node.right. Call the walk function with root tree1 and tree2, finally return arr

## Solution

```

def tree_intersection(tree1, tree2):
    arr = []
    hashtable = HashTable()

    if tree1.root == None or tree2.root == None:
        return 'Tree is empty'

    def walk(node):
        if hashtable.contains(str(node.value)):
            arr.append(node.value)
        else:
            hashtable.add(str(node.value), True)

        if node.left:
            walk(node.left)
        if node.right:
            walk(node.right)
    walk(tree1.root)
    walk(tree2.root)

    return arr


```

## Pull Request

https://github.com/Faisal-Kushha/data-structures-and-algorithms/pull/41
