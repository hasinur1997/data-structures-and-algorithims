class Stack:
    def __init__(self):
        self.items = [None] * 5
        self.size = -1
        self.limit = 5

    def push(self, item):
        if self.is_full():
            raise Exception("Stack overflow")

        self.size += 1
        self.items[self.size] = item

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")

        item = self.items[self.size]
        self.size -= 1

        return item
    
    def peek(self):
        return self.items[self.size]

    def is_empty(self):
        return self.size < 0

    def is_full(self):
        return self.size > self.limit
