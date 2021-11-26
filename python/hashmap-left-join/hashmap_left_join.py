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


def left_join(hashtable_one, hashtable_two):
    arr1 = []
    # __dict__
    # __iter__
    # if hashtable_one.buckets == hashtable_one.size*[None] or hashtable_two.buckets == hashtable_two.size*[None]:
    if hashtable_one.__dict__['buckets'] == hashtable_one.__dict__['size']*[None] or hashtable_two.__dict__['buckets'] == hashtable_two.__dict__['size']*[None]:
        return 'Hash table is empty'
    for item in hashtable_one.__dict__['buckets']:
        if item:
            arr2 = []
            arr2.append(item.head.value[0])
            arr2.append(hashtable_one.get(item.head.value[0]))
            arr2.append(hashtable_two.get(item.head.value[0]))
            arr1.append(arr2)
    return arr1


if __name__ == "__main__":
    hashtable_one = HashTable()
    hashtable_one.add('fond', 'enamored')
    hashtable_one.add('wrath', 'anger')
    hashtable_one.add('diligent', 'employed')
    hashtable_one.add('outfit', 'garb')
    hashtable_one.add('guide', 'usher')
    hashtable_two = HashTable()
    hashtable_two.add('fond', 'averse')
    hashtable_two.add('wrath', 'delight')
    hashtable_two.add('diligent', 'idle')
    hashtable_two.add('guide', 'follow')
    hashtable_two.add('flow', 'jam')

    print(left_join(hashtable_one, hashtable_two))
