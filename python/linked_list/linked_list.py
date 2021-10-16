class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_


class LinkedList:
    """
    Add a node to the head of the linked list
    """

    def __init__(self):
        self.head = None

    def insert(self, value):

        self.head = Node(value, self.head)
        print(self.head.value)

    def includes(self, value):
        """
        Return True if the value is the Linked list and False if the value in not in the Linked list
        """
        the_list = self.head
        while the_list:
            if the_list.value == value:
                return True
            the_list = the_list.next_
        return False

    def __str__(self):
        """
        Loop over all the nodes and print all the values in one line
        """
        output = ""
        the_list = self.head
        while the_list:
            value = str(the_list.value)
            if the_list.next_ == None:
                output = output + '{ ' + value + ' } -> NULL'
                break
            else:
                the_list = the_list.next_
                output = output + '{ ' + value + ' } -> '
        return output


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.__str__()

#     def reverse_list(ll):
#         # method body here

#         arr = ll[::-1]
#         return arr
