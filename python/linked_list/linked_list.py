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

    def append(self, value='null'):
        """
        Add a node to the end of the linked list
        """
        node = Node(value)
        if not self.head:
            self.head = node

        else:
            the_list = self.head
            while the_list.next_ != None:
                the_list = the_list.next_
            the_list.next_ = node

    def insert_before(self, value, new_value):
        """
        adds a new node with the given new value immediately before the first node that has the value specified.
        """
        the_list = self.head
        if the_list.value == value:
            self.insert(new_value)
        else:
            while the_list:
                if the_list.next_.value == value:
                    next_value = the_list.next_
                    the_list.next_ = Node(new_value)
                    the_list.next_.next_ = next_value
                    break
                the_list = the_list.next_

    def insert_after(self, value, new_value):
        """
        Adds a new node with the given new value immediately after the first node that has the value specified.
        """
        the_list = self.head
        while the_list:
            if the_list.value == value:
                next_value = the_list.next_
                the_list.next_ = Node(new_value)
                the_list.next_.next_ = next_value
                break
            the_list = the_list.next_

    def kth(self, k):
        the_list = self.head
        length = 0
        while the_list:
            if length == k:
                return the_list.value
            length += 1
            the_list = the_list.next_
        if k == length:
            return "k value and the length of the list are the same"
        elif k > length:
            return "k value is greater than the length of the linked list"
        elif k < 0:
            return "k value is not a positive integer"
        else:
            return 0

    def zip(self, a, b):
        first_list = a.head
        second_list = b.head
        while first_list != None and second_list != None:
            first_next = first_list.next_
            second_next = second_list.next_
            first_list.next_ = second_list
            second_list.next_ = first_next
            first_list = first_next
            second_list = second_next
            b.head = second_list

    # def reverseList(self):
    #     new_list = []
    #     current = self.head
    #     list2 = LinkedList()
    #     while current:
    #         new_list = new_list + [current.value]
    #         current = current.next_
    #     list2.insert(new_list[- 1])
    #     for i in range(len(new_list) - 1):
    #         list2.append(new_list[- 2 - i])
    #     return (f'head->{list2}')

    # def reverseList(self):

    #     first = self.head
    #     while first != None:
    #         second = first.next_
    #         third = second.next_
    #         forth = third.next_
    #         first = forth
    #     return (f'head->{self}')


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.__str__()
    print(ll.reverseList())
