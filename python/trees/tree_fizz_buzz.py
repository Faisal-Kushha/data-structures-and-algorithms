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


class k_ary_tree:
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


def fizz_buzz_tree(k_ary_tree):
    """
    function called fizz buzz tree
    Arguments: k-ary tree
    Return: new k-ary tree
    """
    try:
        tree = []
        for i in k_ary_tree:
            if i % 3 == 0 and i % 5 == 0:
                tree += ["FizzBuzz"]
            elif i % 3 == 0:
                tree += ["Fizz"]
            elif i % 5 == 0:
                tree += ["Buzz"]
            else:
                tree += [str(i)]
        return tree
    except:
        print("Invalid Input")
        return None
