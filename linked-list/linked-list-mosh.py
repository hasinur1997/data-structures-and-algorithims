class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_fist(self, item):
        node = Node(item)

        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_last(self, item):
        node = Node(item)

        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node

    def remove_first(self):
        if self.head is None:
            raise Exception('List is empty')

        self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            raise Exception('List is empty')

        if self.head.next is None:
            self.head = None

        else:
            current = self.head

            while current.next.next:
                current = current.next

            current.next = None

    def index_of(self, item):
        index = 0

        current = self.head

        while current:
            if current.val == item:
                return index
            index += 1
            current = current.next

        return -1

    def contains(self, item):
        return self.index_of(item) != -1

    def get_kth(self, k):
        first = second = self.head

        for i in range(k-1):
            if not first:
                return -1
            first = first.next

        if not first:
            return -1

        while first.next:
            first = first.next
            second = second.next

        return second.val

    def get_middle(self):
        first = second = self.head

        while first and first.next:
            first = first.next.next
            second = second.next

        return second.val

    def has_circle(self):
        first = second = self.head

        while first and first.next:
            first = first.next.next
            second = second.next

            if first == second:
                return True

        return False

    def reverse(self):
        if self.head is None:
            raise Exception('List is empty')

        current = self.head
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current

            current = next

        self.head = prev

    def print(self):
        if self.head is None:
            raise Exception('List is Empty, nothing to print')

        current = self.head

        while current:
            print(current.val, end=' ')

            current = current.next


li = LinkedList()

li.insert_last(10)
li.insert_last(39)
li.insert_last(20)
li.insert_last(90)
li.insert_last(1200)
# li.insert_last(130)


print(li.has_circle())



