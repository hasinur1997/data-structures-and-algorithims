class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(x)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if self.stack1:
            return self.stack1.pop()

        return -1


