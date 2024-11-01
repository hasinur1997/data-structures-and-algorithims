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


def print_list(head):
    if head is None:
        return

    current = head

    while current:
        print(current.val)
        current = current.next


def revers_list(head, left, right):
    if head is None:
        return head

    counter = 1
    current = head

    while counter < (left - 1):
        current = current.next
        counter += 1

    # print(current.val)

    temp = current.next
    first = current
    prev = None
    current = current.next

    # print(first.val)

    while counter < right-1:
        next = current.next
        current.next = prev
        prev = current
        current = next
        counter += 1

    # print(current.val)
    temp.next = current.next
    first.next = current
    # print(head.next.next.val)
    return head





l1 = LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)
# l1.display()

new_head = revers_list(l1.head, 2, 4)
# print_list(new_head)

# print("sdf")