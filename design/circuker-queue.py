class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.counter = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.counter += 1

        return True

    def deQueue(self) -> bool:

        if self.isEmpty():
            return False
        self.head = self.head.next
        self.counter -= 1

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.counter == 0

    def isFull(self) -> bool:
        return self.counter >= self.size



mycirculer = MyCircularQueue(3)

print(mycirculer.enQueue(1))
print(mycirculer.enQueue(2))
print(mycirculer.enQueue(3))
print(mycirculer.enQueue(4))
print(mycirculer.Rear())
print(mycirculer.isFull())
print(mycirculer.deQueue())
print(mycirculer.enQueue(4))
print(mycirculer.Rear())