from ..stack.stack import Stack

class Queue:
    def __init__(self):
        self.capacity = 5
        self.count = 0
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')

        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

        return self.stack2.pop()
        
    def peek(self):
        if self.is_empty():
            raise Exception('Queue is empty')

        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

        return self.stack2.peek()
        
    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def is_full(self):
        return self.count == self.capacity


q = Queue()
q.enqueue(20)
q.enqueue(203)
q.enqueue(200)
q.enqueue(40)
q.enqueue(66)

print(q.stack1.items)
