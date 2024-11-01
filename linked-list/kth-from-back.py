class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head):

        current = head

        stack = []

        while current:
            length = len(stack)
            while stack and stack[-1] < current.val:
                stack.pop()
            stack.append(current.val)
            current = current.next

        dummy = ListNode(0)

        current = dummy

        while stack:
            node = ListNode(stack.pop(0))

            current.next = node

            current = current.next

        return dummy.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(8)
node6 = ListNode(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


def kth_node(head, k):
    p1 = p2 = head

    index = 1

    while index < k:
        if not p1:
            break

        p1 = p1.next
        index += 1

    if index < k:
        return False

    while p1.next:
        p1 = p1.next
        p2 = p2.next

    return p2


def middle_node(head):
    p1 = p2 = head

    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next

    return p1


def swap_node_pairs(head):
    if head is None:
        return

    current = head

    while current and current.next:

        if current.val != current.next.val:
            current.val, current.next.val = current.next.val, current.val

        current = current.next.next

    return head


def print_list(head):
    if head is None:
        return

    print(head.val)

    print_list(head.next)


node = swap_node_pairs(node1)

print_list(node)
