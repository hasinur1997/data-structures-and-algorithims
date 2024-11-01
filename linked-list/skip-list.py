class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Skiplist:

    def __init__(self):
        self.head = None

    def search(self, target: int) -> bool:
        if self.head is None:
            return False

        current = self.head

        while current:
            if current.val == target:
                return True
            current = current.next

        return False

    def add(self, num: int) -> None:
        node = Node(num)

        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = node

    def erase(self, num: int) -> bool:

        if self.head is None:
            return False

        if self.head.val == num:
            self.head = self.head.next
            return True

        current = self.head
        prev = None

        while current:
            if current.val == num:
                prev.next = current.next
                return True

            prev = current
            current = current.next

        return False



li = Skiplist()
li.add(1)
li.add(2)
li.add(3)

print(li.search(0))
li.add(4)
print(li.search(1))
print(li.erase(0))
print(li.erase(1))
print(li.search(1))