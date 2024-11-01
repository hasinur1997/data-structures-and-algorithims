# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def append(self, val):
#         node = Node(val)
#
#         if self.head is None:
#             self.head = node
#
#         else:
#             current = self.head
#             while current.next is not None:
#                 current = current.next
#
#             current.next = node
#
#     def prepend(self, val):
#         node = Node(val)
#
#         if self.head is None:
#             self.head = node
#         else:
#             node.next = self.head
#             self.head = node
#
#     def insert_at(self, val, position):
#         # if position < 1 or position > self.len():
#         #     raise Exception("Invalid Index")
#
#         node = Node(val)
#
#         if position == 1:
#             node.next = self.head
#             self.head = node
#
#         else:
#             count = 1
#             prev = self.head
#
#             while count < position - 1:
#                 prev = prev.next
#                 count += 1
#
#             current = prev.next
#             node.next = current
#             prev.next = node
#
#     def delete_first(self):
#         if self.head is None:
#             return False
#
#         temp = self.head
#         self.head = temp.next
#
#         return temp
#
#     def delete_last(self):
#         if self.head is None:
#             return False
#
#         current = self.head
#         prev = None
#
#         while current.next is not None:
#             prev = current
#             current = current.next
#
#         prev.next = current.next
#
#         return current
#
#     def delete_at(self, position):
#
#         if self.head is None:
#             return False
#
#         if position == 1:
#             temp = self.head
#             self.head = temp.next
#             return temp
#         else:
#             counter = 1
#             prev = self.head
#
#             while counter < position - 1:
#                 prev = prev.next
#                 counter += 1
#
#             current = prev.next
#             prev.next = current.next
#
#             return current
#
#     def reverse(self):
#         if self.head is None:
#             return False
#
#         current = self.head
#         prev = None
#         next = None
#
#         while current is not None:
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#
#         self.head = prev
#
#     def remove_dup_sort(self):
#         if self.head is None:
#             return False
#
#         current = self.head
#
#         while current is not None and current.next is not None:
#             if current.val == current.next.val:
#                 current.next = current.next.next
#             else:
#                 current = current.next
#
#     def insert_into_sorted(self, val):
#         if self.head is None:
#             return False
#
#         current = self.head
#         node = Node(val)
#         temp = None
#
#         while current is not None and current.val < node.val:
#             temp = current
#             current = current.next
#
#         temp.next = node
#         node.next = current
#
#     def remove_middle(self):
#         if self.head is None:
#             return False
#         fast = self.head
#         slow = self.head
#         prev = self.head
#
#         while fast and fast.next:
#             prev = slow
#             slow = slow.next
#             fast = fast.next.next
#
#         prev.next = slow.next
#
#     def nth_from_end(self, position):
#         if self.head is None:
#             return False
#
#         first = self.head
#         second = self.head
#
#         counter = 0
#
#         while counter < position:
#             first = first.next
#             counter += 1
#
#         while first is not None:
#             first = first.next
#             second = second.next
#
#         return second
#
#
#     def len(self):
#         counter = 0
#
#         current = self.head
#         while current is not None:
#             counter += 1
#
#         return counter
#
#     def print(self):
#
#         if self.head is None:
#             print("List is empty. Nothing to print")
#         else:
#             current = self.head
#
#             while current is not None:
#                 print(current.val)
#                 current = current.next
#
#
# l1 = LinkedList()
# l1.append(1)
# l1.append(2)
# l1.append(6)
# l1.append(10)
#
# l2 = LinkedList()
# l2.append(4)
# l2.append(5)
# l2.append(7)
#
# l3 = LinkedList()
# l3.append(9)
# l3.append(11)
# l3.append(15)
# l3.append(19)
#
#
# def merge_two_list(l1, l2):
#     dummy_head = Node(None)
#     current = dummy_head
#
#     while l1 and l2:
#         if l1.val <= l2.val:
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = l2
#             l2 = l2.next
#
#         current = current.next
#
#     if l1:
#         current.next = l1
#
#     if l2:
#         current.next = l2
#
#     return dummy_head.next
#
#
# # merged = merge_two_list(l1.head, l2.head)
# # merged1 = merge_two_list(merged, l3.head)
#
#
# linked_lists = [l1.head, l2.head, l3.head]
#
# def merge_k_list(ls):
#     if not ls:
#         return None
#     merged = None
#
#     for li in ls:
#         merged = merge_two_list(merged, li)
#
#     return merged
#
#
#
# kmerged = merge_k_list(linked_lists)
#
# while kmerged:
#     print(kmerged.val)
#     kmerged = kmerged.next
#
#
#

# y = [4, 5, 1j];
#
# y.sort();

s = {10, 20, 30, 40, 50}

print(sum(s))