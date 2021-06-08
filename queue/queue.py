# Class Queue
class Queue:
    # Initialize
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.data = []
        self.queue_max = 5

    # Add item at top of the queue
    def enqueue(self, item):
        self.data.insert(self.rear, item)
        self.rear += 1

    # Remove item from front
    def dequeue(self):
        if self.rear == self.front:
            print("The queue is empty")
            return
        self.front += 1

    # Print the queue
    def print_queue(self):
        for i in range(self.front, self.rear):
            print(self.data[i])