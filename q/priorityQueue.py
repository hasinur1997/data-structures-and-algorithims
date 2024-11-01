class Queue:
    def __init__(self):
        self.capacity = 5
        self.counter = 0
        self.items = [None] * self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")

        for i in range(len(self.items)-1):
            if self.items[i] > item:
                self.items[i+1] = self.items[i]
            else:
                break

        self.items[i] = item
        self.counter += 1

    def dequeue(self):
        pass

    def is_empty(self):
        pass

    def is_full(self):
        return self.counter == self.capacity

    def peek(self):
        return self.items[self.counter]


q = Queue()
q.enqueue(10)
q.enqueue(1)
q.enqueue(50)
q.enqueue(190)

print(q.items)
