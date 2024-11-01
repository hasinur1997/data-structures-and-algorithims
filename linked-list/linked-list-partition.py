class ListNode:
    def __init__(self, val = None):
        self.next = None
        self.val = val


def find_middle(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(head1, head2):

    dummy_head = ListNode()
    current = dummy_head

    while head1 and head2:
        if head1.val <= head2.val:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next

        current = current.next

    if head1:
        current.next = head1

    if head2:
        current.next = head2

    return dummy_head.next


def merge_sort(head):
    if not head or not head.next:
        return head

    mid = find_middle(head)
    left = head
    right = mid.next
    mid.next = None

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def print_list(head):
    current = head

    while current is not None:
        print(current.val)
        current = current.next


node1 = ListNode(10)
node2 = ListNode(12)
node3 = ListNode(14)
node4 = ListNode(20)
node5 = ListNode(40)

n1 = ListNode(1)
n2 = ListNode(4)
n3 = ListNode(10)
n4 = ListNode(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

n1.next = n2
n2.next = n3
n3.next = n4


head = node1
head2 = n1

new_head = merge_sort(head)

print_list(new_head)


