class Conversation:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity

        self.array = []

        self.output = []

        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_empty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.is_empty():
            self.top -= -1
            return self.array.pop()

        else:
            return '$'

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def is_operand(self, ch):
        return ch.isalpha()

