class Stack:
    def __init__(self, size):
        self.data = [None] * size
        self.counter = -1

    def push(self, item):
        if self.is_full():
            exit('Stack is full')

        while self.peek() > item:
            self.pop()

        self.counter += 1
        self.data[self.counter] = item

    def pop(self):
        if self.is_empty():
            exit('Stack is empty')

        item = self.data[self.counter]
        self.data[self.counter] = None
        self.counter -= 1

        return item

    def is_full(self):
        return self.counter == len(self.data)

    def is_empty(self):
        return self.counter == -1

    def peek(self):
        if self.is_empty():
            return False

        return self.data[self.counter]




stack = Stack(5)
stack.push(1)
stack.push(4)
stack.push(5)
stack.push(3)
stack.push(12)
stack.push(10)

print(stack.data)
