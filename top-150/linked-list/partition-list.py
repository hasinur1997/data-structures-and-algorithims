class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, item):
        node = ListNode(item)

        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node

    def display(self):
        if self.head is None:
            return

        current = self.head

        while current:
            print(current.val)
            current = current.next


def partition(head, x):
    if head is None:
        return head

    dummy = ListNode(0)
    current = dummy

    t = head

    while t:
        if t.val < x:
            current.next = ListNode(t.val)
            current = current.next

        t = t.next

    t = head

    while t:
        if t.val >= x:
            current.next = ListNode(t.val)
            current = current.next

        t = t.next

    return dummy.next


def print_list(head):
    if head is None:
        return

    current = head

    while current:
        print(current.val)
        current = current.next



l1 = LinkedList()
l1.insert(1)
l1.insert(4)
l1.insert(3)
l1.insert(2)
l1.insert(5)
l1.insert(2)

# l1.display()

part = partition(l1.head, 3)

print_list(part)

