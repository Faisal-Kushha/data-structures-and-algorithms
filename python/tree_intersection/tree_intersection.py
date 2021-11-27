class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node


class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None]*size

    def hash(self, key):
        return sum([ord(char) for char in key]) * 7 % self.size

    def add(self, key, value):
        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] = LinkedList()
        my_value = [key, value]
        self.buckets[index].insert(my_value)

    def contains(self, key):
        index = self.hash(key)
        if self.buckets[index]:
            linked_list = self.buckets[index]
            current = linked_list.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False

    def get(self, key):
        index = self.hash(key)
        if self.buckets[index]:
            linked_list = self.buckets[index]
            current = linked_list.head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next
        return None


class Node_tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


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


if __name__ == "__main__":
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

    print(tree_intersection(tree1, tree2))
