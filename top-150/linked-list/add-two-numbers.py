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

            while current:
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


def add_two(head1, head2):
    dummy = Node(0)
    current = dummy
    carry = 0

    while head1 or head2 or carry != 0:
        l1_value = head1.val if head1 else 0
        l2_value = head2.val if head2 else 0
        _sum = l1_value + l2_value + carry
        carry = _sum // 10

        current.next = Node(_sum%10)

        head1 = head1.next if head1 else None
        head2 = head2.next if head2 else None

        current = current.next

    return dummy.next



l1 = Node(2)
node1 = Node(4)
node2 = Node(3)

l1.next = node1
node1.next = node2

l2 = Node(5)
node3 = Node(6)
node4 = Node(4)

l2.next = node3
node3.next = node4



# print_list(l1)
# print_list(l2)

result = add_two(l1, l2)

print_list(result)


