class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        node = Node(val)

        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

    def dequeue(self):
        if self.is_empty():
            return False
        temp = self.head

        self.head = self.head.next

        return temp.val

    def peek(self):
        if self.is_empty():
            return False
        return self.head.val

    def is_empty(self):
        return self.head is None


q = Queue()
q.enqueue(12)
q.enqueue(15)
q.enqueue(50)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.peek())


"""
    1->-1-2->2->3->4->5->6->7->8
    
"""