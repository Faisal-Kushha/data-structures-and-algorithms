class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_


class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, value):
        the_list = self.head
        while the_list:
            if the_list.value == value:
                return True
            the_list = the_list.next_
        return False

    def __str__(self):
        output = ""
        the_list = self.head
        while the_list:
            value = the_list.value
            # if the_list.next_ == None:
            output = output + f"( {value} ) -> NULL"
            # else:
            the_list = the_list.next_
            # output = output + f"( {value} ) -> "

        return output


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.__str__()
