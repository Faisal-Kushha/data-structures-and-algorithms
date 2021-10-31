class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Queue:
    def __init__(self, collection=[]):
        self.value = collection

    def peek(self):
        if len(self.value):
            return True
        return False

    def enqueue(self, item):
        self.value.append(item)

    def dequeue(self):
        return self.value.pop(0)


class BinaryTree:
    def __init__(self):
        self.root = None

    def bfs(self):
        """
        A binary tree method which returns a list of items that it contains
        input: None
        output: tree items
        """
        # Queue queue <-- new Queue()
        queue = Queue()
        # queue.enqueue(root)
        queue.enqueue(self.root)

        list_of_items = []

        while queue.peek():
            front = queue.dequeue()
            list_of_items += [front.value]

            if front.left:
                queue.enqueue(front.left)

            if front.right:
                queue.enqueue(front.right)

        return list_of_items

    def pre_order(self):
        """
        A binary tree method which returns a list of items that it contains
        input: None
        output: tree items
        sub method : walk () to make the recursion staff
        """
        list_of_items = []

        def walk(node):
            if node:
                list_of_items.append(node.value)
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)
            else:
                return "Empty tree"

        walk(self.root)
        return list_of_items

    def in_order(self):
        """
        function to in order the list using Trees
        """
        list_of_items = []

        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                list_of_items.append(node.value)
                if node.right:
                    walk(node.right)
            else:
                return "Empty tree"

        walk(self.root)
        return list_of_items

    def post_order(self):
        """
        A binary tree method which returns a list of items in post order
        input: None
        output: tree items
        """
        list_of_items = []

        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)
                list_of_items.append(node.value)
            else:
                return "Empty tree"

        walk(self.root)
        return list_of_items

    def max_value(self):
        """
        A binary tree method which search for and find the maximum value in the tree
        Arguments: none
        Returns: number
        """
        self.max = 0

        def walk(node):
            if node:
                if node.left:
                    walk(node.left)
                    if node.left.value > self.max:
                        self.max = node.left.value
                if node.right:
                    walk(node.right)
                    if node.right.value > self.max:
                        self.max = node.right.value

        walk(self.root)
        if self.root.value > self.max:
            return self.root.value
        return self.max


class BinarySearchTree(BinaryTree):
    """
    Binary Search Tree class and it's a sub-class of the Binary Tree Class, it has two methods:
    1- Add Method which take:-
    Arguments: value
    Return: nothing

    2- Contains Method which take:-
    Argument: value
    Returns: boolean indicating whether or not the value is in the tree at least once.
    """

    def add(self, value):

        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root

            while current:
                if value > current.value:
                    if not current.left:
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if not current.right:
                        current.right = Node(value)
                        break
                    current = current.right

    def contains(self, value):

        if self.root == None:
            return False
        else:
            current = self.root
            while current:
                if current.value == value:
                    return True
                elif value > current.value:
                    if not current.left:
                        return False
                    current = current.left
                else:
                    if not current.right:
                        return False
                    current = current.right
