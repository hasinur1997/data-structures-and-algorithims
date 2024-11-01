class Heap:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def insert(self, item):
        self.items.append(item)
        self.bubble_up()

    def parent(self, index):
        return self.items[self.parent_index(index)]

    def parent_index(self, index):
        return (index - 1) // 2

    def swap(self, first, second):
        temp = self.items[first]
        self.items[first] = self.items[second]
        self.items[second] = temp

    def remove(self):
        if self.is_empty():
            return False

        if self.size() == 1:
            return self.items.pop()
        item = self.items[0]
        self.items[0] = self.items.pop()
        self.bubble_down()
        return item

    def size(self):
        return len(self.items)

    def bubble_up(self):
        index = self.size() - 1
        while index > 0 and self.items[index] > self.parent(index):
            parent_index = self.parent_index(index)
            self.swap(index, parent_index)
            index = parent_index

    def bubble_down(self):
        index = 0
        while index <= self.size() and not self.valid_parent(index):
            larger_index = self.larger_index(index)
            self.swap(index, larger_index)
            index = larger_index

    def larger_index(self, index):
        if not self.has_left(index):
            return index

        if not self.has_right(index):
            return self.left_index(index)

        return self.left_index(index) if self.left_child(index) > self.right_child(index) else self.right_index(index)

    def valid_parent(self, index):
        if not self.has_left(index):
            return True

        if not self.has_right(index):
            return self.items[index] >= self.left_child(index)

        return self.items[index] >= self.left_child(index) and self.items[index] >= self.right_child(index)

    def left_index(self, index):
        return (index * 2) + 1

    def right_index(self, index):
        return (index * 2) + 2

    def left_child(self, index):
        return self.items[self.left_index(index)]

    def right_child(self, index):
        return self.items[self.right_index(index)]

    def has_left(self, index):
        return self.left_index(index) < self.size() - 1

    def has_right(self, index):
        return self.right_index(index) < self.size()

    def is_empty(self):
        return len(self.items) == 0

heap = Heap()
heap.insert(5)
heap.insert(40)
heap.insert(7)
heap.insert(120)
heap.insert(9)
heap.insert(35)
heap.insert(12)
heap.insert(180)
heap.insert(3)

heap.remove()
heap.remove()
heap.remove()
heap.remove()
heap.remove()
heap.remove()
# heap.remove()
# heap.remove()
# heap.remove()
print(heap)

