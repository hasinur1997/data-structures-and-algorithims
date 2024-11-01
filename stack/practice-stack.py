class Stack:
    def __init__(self, size):
        self.data = [None] * size
        self.counter = -1

    def push(self, item):
        if self.is_full():
            exit('Stack is full')
        self.counter += 1
        self.data[self.counter] = item

    def pop(self):
        if self.is_empty():
            exit('Stack is empty')
        self.counter -= 1
        return self.data.pop()

    def is_empty(self):
        return self.counter == -1

    def len(self):
        return self.counter

    def is_full(self):
        return self.counter == len(self.data) - 1

    def peek(self):
        if self.is_empty():
            exit('Stack is empty')
        return self.data[self.counter]


stack = Stack(5)
stack.push(20)
stack.push(120)
stack.push(60)
stack.push(40)
stack.push(150)
stack.push(150)




