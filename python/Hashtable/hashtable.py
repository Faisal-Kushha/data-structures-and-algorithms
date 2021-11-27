"""
The implementation of Node class, Linked list class, and Hashmap class.
"""
import re
from typing import Text


class Node:
    def __init__(self, value=None, next_=None):
        """
      Initalization the Node
      """
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = Node(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        """
        Initalization of Hash table

        """
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pari in a Node at that index.
        """
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value
        Return : No return value
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
            self.__buckets[index] = LinkedList()
        my_value = [key, value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
        """
        Retrieve the most recent value of in oour hasmap for the given key

        :param key str
        :rvalue any
        """
        # calculate index
        index = self.__hash(key)
        # check if there is a non empty bucket at the index
        if self.__buckets[index]:
            # iterate over linked list
            linked_list = self.__buckets[index]
            current = linked_list.head
            while current:
                # check if the key in each node matches
                if current.value[0] == key:
                    # return the value of the node with the mathcing key
                    return current.value[1]
                current = current.next

        # return None
        return None

    def contains(self, key):
        # calculate index
        index = self.__hash(key)
        # check if there is a non empty bucket at the index
        if self.__buckets[index]:
            # iterate over linked list
            linked_list = self.__buckets[index]
            current = linked_list.head
            while current:
                # check if the key in each node matches
                if current.value[0] == key:
                    # return the value of the node with the mathcing key
                    return True
                current = current.next

        # return None
        return False


def repeated_word(text=None):
    Hash_Table = HashTable()
    if text is not None:
        text = re.sub('\W+', ' ', text).lower().split()
        max_word = 0
        new_word = ''
        for word in text:
            counter = 0
            if Hash_Table.contains(word):
                temp = Hash_Table.get(word)
                temp = temp + 1
                Hash_Table.add(word, temp)
                if temp > max_word:
                    max_word = temp
                    new_word = word
            else:
                Hash_Table.add(word, counter+1)

        return new_word, max_word


if __name__ == "__main__":

    # text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    text = "No. Try not. Do or do not. There is no try."
    print(repeated_word(text))
