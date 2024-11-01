class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def replace_node(head):
    if head is None:
        return

    odd_head = head
    even_head = head.next

    odd = odd_head
    even = even_head

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head

    return odd_head

def print_list(head):
    if head is None:
        return

    print(head.val)

    print_list(head.next)

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

new_head = replace_node(node1)

print_list(new_head)



