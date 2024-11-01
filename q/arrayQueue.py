class Queue:
    
    def __init__(self):
        self.capacity = 5
        self.items = [None] * self.capacity
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception('Queue is full')

        self.items[self.rear] = item
        self.rear += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        
        item = self.items[self.front]
        self.front += 1

        return item
        
    def peek(self):
        return self.items[self.front]

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return self.rear == self.capacity


q = Queue()
q.enqueue(20)
q.enqueue(50)
q.enqueue(120)
q.enqueue(30)
q.enqueue(70)

print(q.peek())