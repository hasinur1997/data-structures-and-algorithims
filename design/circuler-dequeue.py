class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.counter = 0
        self.items = []

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.items.insert(0, value)
        self.counter += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.items.append(value)
        self.counter += 1

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.items.pop(0)
        self.counter -= 1

        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.items.pop()
        self.counter -= 1

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.items[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.items[len(self.items) - 1]

    def isEmpty(self) -> bool:
        return self.counter == 0

    def isFull(self) -> bool:
        return self.counter >= self.size



"""
    ["MyCircularDeque","insertFront","getFront","isEmpty","deleteFront","insertLast","getRear","insertLast","insertFront","deleteLast","insertLast","isEmpty"]

"""
queue = MyCircularDeque(8)

print(queue.insertFront(5))
print(queue.getFront())
print(queue.isEmpty())
print(queue.deleteFront())
print(queue.items)