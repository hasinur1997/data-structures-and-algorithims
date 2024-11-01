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


l1 = LinkedList()
l1.insert(1)
# l1.insert(2)
# l1.insert(3)
# l1.insert(4)
# l1.insert(5)


def remove_from_end(head, n):
    fast = slow = head

    for i in range(n):
        fast = fast.next

    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return head

def print_list(head):
    if head is None:
        return

    current = head

    while current:
        print(current.val)
        current = current.next


new = remove_from_end(l1.head, 1)

print_list(new)
