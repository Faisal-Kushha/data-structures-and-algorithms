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


def left_join(hashmap1, hashmap2):
    arr1 = []
    if hashmap1.buckets == hashmap1.size*[None] or hashmap2.buckets == hashmap2.size*[None]:
        return 'Hash table is empty'
    for item in hashmap1.buckets:
        if item:
            arr2 = []
            arr2.append(item.head.value[0])
            arr2.append(hashmap1.get(item.head.value[0]))
            arr2.append(hashmap2.get(item.head.value[0]))
            arr1.append(arr2)
    return arr1


if __name__ == "__main__":
    hashmap1 = HashTable()
    hashmap1.add('fond', 'enamored')
    hashmap1.add('wrath', 'anger')
    hashmap1.add('diligent', 'employed')
    hashmap1.add('outfit', 'garb')
    hashmap1.add('guide', 'usher')
    hashmap2 = HashTable()
    hashmap2.add('fond', 'averse')
    hashmap2.add('wrath', 'delight')
    hashmap2.add('diligent', 'idle')
    hashmap2.add('guide', 'follow')
    hashmap2.add('flow', 'jam')

    print(left_join(hashmap1, hashmap2))
