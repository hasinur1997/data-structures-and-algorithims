class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


node = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(6)

node.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node3


def print_list(head):
    if head is None:
        return

    current = head

    while current:
        current = current.next


def has_cycle(head):
    if head is None:
        return False

    first = slow = head

    while first and first.next:
        print(first.val)
        first = first.next.next
        slow = slow.next

        if first == slow:
            return True

    return False


print(has_cycle(node))

# print_list(node)
