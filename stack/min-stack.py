class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        n = len(self.data) - 1

        return self.data[n]

    def getMin(self) -> int:
        return min(self.data)


stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)

print(stack.getMin())
print(stack.pop())
print(stack.top())
print(stack.getMin())

