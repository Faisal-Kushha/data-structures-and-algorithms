# Stacks and Queues

# Node

[x] Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

# Stack

[x] Create a Stack class that has a top property. It creates an empty Stack when instantiated.

[x] This object should be aware of a default empty value assigned to top when the stack is created.

[x] The class should contain the following methods:

## push

[x] Arguments: value

[x] adds a new node with that value to the top of the stack with an O(1) Time performance.

## pop

[x] Arguments: none

[x] Returns: the value from node from the top of the stack

[x] Removes the node from the top of the stack

[x] Should raise exception when called on empty stack

## peek

[x] Arguments: none

[x] Returns: Value of the node located at the top of the stack

[x] Should raise exception when called on empty stack

## is empty

[x] Arguments: none

[x] Returns: Boolean indicating whether or not the stack is empty.

# Queue

[x] Create a Queue class that has a front property. It creates an empty Queue when instantiated.

[x] This object should be aware of a default empty value assigned to front when the queue is created.

[x] The class should contain the following methods:

## enqueue

[x] Arguments: value

[x] adds a new node with that value to the back of the queue with an O(1) Time performance.

## dequeue

[x] Arguments: none

[x] Returns: the value from node from the front of the queue

[x] Removes the node from the front of the queue

[x] Should raise exception when called on empty queue

## peek

[x] Arguments: none

[x] Returns: Value of the node located at the front of the queue

[x] Should raise exception when called on empty stack

## is empty

[x] Arguments: none

[x] Returns: Boolean indicating whether or not the queue is empty

# Testing

[x] Can successfully push onto a stack

[x] Can successfully push multiple values onto a stack

[x] Can successfully pop off the stack

[x] Can successfully empty a stack after multiple pops

[x] Can successfully peek the next item on the stack

[x] Can successfully instantiate an empty stack

[x] Calling pop or peek on empty stack raises exception

[x] Can successfully enqueue into a queue

[x] Can successfully enqueue multiple values into a queue

[x] Can successfully dequeue out of a queue the expected value

[x] Can successfully peek into a queue, seeing the expected value

[x] Can successfully empty a queue after multiple dequeues

[x] Can successfully instantiate an empty queue

[x] Calling dequeue or peek on empty queue raises exception

# Pull Request

https://github.com/Faisal-Kushha/data-structures-and-algorithms/pull/28
