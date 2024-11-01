class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        node = Node(val)

        if self.top is None:
            self.top = node
        else:
            temp = self.top
            node.next = temp
            self.top = node

    def pop(self):
        if self.is_empty():
            return False

        temp = self.top
        self.top = self.top.next

        return temp.val

    def peek(self):
        if self.is_empty():
            return False

        return self.top.val

    def is_empty(self):
        return self.top is None


stack = Stack()
stack.push(10)
stack.push(12)
stack.push(14)
stack.push(15)
stack.push(16)


