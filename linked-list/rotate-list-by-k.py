class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(node):
    if node is None:
        print()
        return
    print(node.val, end=' ')

    print_list(node.next)


def rotate_list(head, k):

    if k == 0:
        return head

    p1 = p2 = head

    while k >= 0 and p2 is not None:
        p2 = p2.next
        k -= 1

    while p2 and p2.next:
        p2 = p2.next
        p1 = p1.next

    if p2 is None:
        return head

    p2.next = head
    head = p1.next

    p1.next = head

    return head



node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
# node4 = ListNode(4)
# node5 = ListNode(5)

node1.next = node2
node2.next = node3
# node3.next = node4
# node4.next = node5

print_list(node1)

# new_head = rotate_list(node1, 1)
new_head = rotate_list(node1, 4)

print_list(new_head)


