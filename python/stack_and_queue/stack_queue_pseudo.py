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
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top == None:
            raise Empty("Empty stack")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):
        return self.top.value

    def is_empty(self):
        return not self.top


class PseudoQueue:
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()

    def enqueue(self, value):
        self.front.push(value)

    def dequeue(self):

        if self.front.top == None:
            raise Empty("Empty")
        while self.front.top:
            self.rear.push(self.front.pop())

        return self.rear.pop

    def __str__(self):
        output = ""
        current = self.front.top
        while current:
            if current.next == None:
                output = output + "{ " + current.value + " }"
                current = current.next
            else:
                output = output + "{ " + current.value + " } -> "
                current = current.next
        return output


if __name__:
    "__main__"

queue = PseudoQueue()
queue.enqueue(20)
queue.enqueue(15)
queue.enqueue(10)
queue.enqueue(5)
queue.dequeue()
