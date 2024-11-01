class MaxHeap:

    def __init__(self):
        self.data = []

    def insert(self, item):
        self.data.append(item)
        self.bubble_up()

    def remove(self):
        if len(self.data) == 0:
            return False

        if len(self.data) == 1:
            return self.data.pop()

        item = self.data[0]
        self.data[0] = self.data.pop()

        self.bubble_up()

        return item


    def bubble_up(self):

        index = len(self.data) - 1
        parent_index = (index - 1) // 2

        while index > 0 and self.data[index] > self.data[parent_index]:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            index = parent_index
            parent_index = (index - 1) // 2


heap = MaxHeap()
heap.insert(1)
heap.insert(3)
heap.insert(5)
heap.insert(8)
heap.insert(10)


print(heap.remove())
print(heap.remove())
print(heap.remove())
print(heap.remove())
print(heap.remove())
print(heap.remove())

