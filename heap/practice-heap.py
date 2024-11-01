class Heap:
    def __init__(self):
        self.data = []

    def insert(self, item):
        self.data.append(item)

        self.swim()

    def remove(self):
        if not self.data:
            return

        if len(self.data) <= 1:
            return self.data.pop()

        max_item = self.data[0]

        self.data[0] = self.data.pop()

        self.sink()

        return max_item

    def swim(self):
        index = len(self.data) - 1

        parent_index = (index - 1) // 2
        while index > 0 and self.data[index] > self.data[parent_index]:
            self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
            index = parent_index
            parent_index = (index - 1) // 2


    def sink(self):
        index = 0
        n = len(self.data)
        while True:
            large = index
            l = 2 * index + 1
            r = 2 * index + 2

            if l < n and self.data[l] > self.data[large]:
                large = l

            if r < n and self.data[r] > self.data[large]:
                large = r

            if index != large:
                self.data[index], self.data[large] = self.data[large], self.data[index]
                index = large
            else:
                break


heap = Heap()
heap.insert(4)
heap.insert(5)
heap.insert(6)
heap.insert(7)
heap.insert(8)
heap.insert(9)

print(heap.remove())
print(heap.remove())
print(heap.remove())
print(heap.remove())
print(heap.remove())
print(heap.remove())
print(heap.remove())
print(heap.remove())
print(heap.data)
