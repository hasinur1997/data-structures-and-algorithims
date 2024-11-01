class Queue:
    def __init__(self, size):
        self.data = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, item):
        if self.is_full():
            exit('Queue is full')

        if self.is_empty():
            self.front += 1

        self.rear += 1
        self.data[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            exit('Queue is empty')

        item = self.data[self.front]
        self.front += 1

        return item

    def is_empty(self):
        return (self.front == -1) or (self.front == len(self.data))

    def is_full(self):
        return self.rear == len(self.data) - 1

    def peek(self):
        if self.is_empty():
            exit('Queue is empty')

        return self.data[self.front]


q = Queue(5)
q.enqueue(20)
q.enqueue(5)
q.enqueue(90)
q.enqueue(12)
q.enqueue(75)
# q.enqueue(75)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()

print(q.peek())
