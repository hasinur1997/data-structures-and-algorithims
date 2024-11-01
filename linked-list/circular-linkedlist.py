class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class CirCularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        node = Node(val)

        if not self.head:
            self.head = node
        else:
            self.tail = node

        self.tail.next = self.head

    def print(self):

        current = self.head

        while current.next is not self.head:
            print(current.val)
            current = current.next

        print(current.val)


circular = CirCularLinkedList()
circular.insert(10)
circular.insert(12)
circular.insert(40)
circular.print()
print("H")


head = None
tail = None

