# Definition for singly-linked list.
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

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
solution.removeNodes(node1)


def print_list(head):
    if not head:
        return

    print(head.val)

    if head.next:
        print_list(head.next.next)


print_list(node1)
