class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Empty(Exception):
    pass


class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Adding value to the stack
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
        Removing value from the stack
        """
        if self.top == None:
            raise Empty("Empty stack")
            # Or I can use this one instead od creating a class for empty stack: raise Exception("Empty stack")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        """
        Viewing the value of the top Node in the stack.
        """
        return self.top.value

    def is_empty(self):
        """
        It will return true when stack is empty otherwise it will return false.
        """
        return not self.top


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        """
        Adding Nodes or items to the rear side of queue.
        """
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """
        Removing Nodes or items from the front side of queue.
        """
        if self.front == None:
            raise Empty("Empty stack")
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        """
        Viewing the value of the front Node in the queue.
        """
        return self.front.value

    def is_empty(self):
        """
        It will return true when queue is empty otherwise it will return false.
        """
        return not self.front


if __name__:
    "__main__"

data = [1, 2, 3, "car"]
data.pop()
