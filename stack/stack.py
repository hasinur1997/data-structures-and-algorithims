# Class Stack
class Stack:
    # Initialize Stack
    def __init__(self):
        self.data = []
        self.stack_max = 10
        self.top = 0

    # Add item at the top
    def push(self, item):
        if self.top < self.stack_max:
            self.data.insert(self.top, item)
            self.top += 1
        else:
            print("Stack is full")

    # Remove item from top of the stack
    def pop(self):
        item = None
        if self.top == 0:
            print("Stack is empty")
            return

        self.top -= 1
        item = self.data[self.top]

        return item

    # Display all item in stack
    def print_stack(self):
        if self.top == 0:
            print("Stack is empty")
            return

        for i in range(self.top-1, 0-1, -1):
            print(self.data[i])
