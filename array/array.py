class Array:
    def __init__(self):
        self.length = 2
        self.data = [None] * 2
        self.count = 0

    def insert(self, item):
        # Resize the array
        if self.count == self.length:
            self.length = self.count * 2
            new_array = [None] * self.length

            for i in range(self.count):
                new_array[i] = self.data[i]
            self.data = new_array

        # insert item
        self.data[self.count] = item
        self.count += 1

    def insert_at(self, item, index):
        # Resize the array
        if (self.count + 1) == self.length:
            self.length = self.count * 2
            new_array = [None] * self.length

            for i in range(self.count):
                new_array[i] = self.data[i]
            self.data = new_array

        for i in range(self.count, index-1, -1):
            self.data[i+1] = self.data[i]

        self.data[index] = item
        self.count += 1

    def remove_at(self, index):
        if index < 0 or index > self.count:
            raise IndexError('Index out range')

        for i in range(index, self.count):
            self.data[i] = self.data[i+1]

        self.count -= 1

    def index_of(self, item):
        for i in range(self.count):
            if item == self.data[i]:
                return i

        return -1

    def max(self):
        _max = self.data[0]

        for num in self.data:
            if num and num > _max:
                _max = num

        return _max

    def min(self):
        _min = self.data[0]

        for num in self.data:
            if num and num < _min:
                _min = num

        return _min

    def reverse(self):
        new_items = [None] * self.count
        x = 0
        for i in range(self.count-1, -1, -1):
            new_items[x] = self.data[i]
            x += 1
        self.data = new_items

    def print(self):
        for i in range(self.count):
            print(self.data[i], end=" ")


items = Array()
items.insert(10)
items.insert(20)
items.insert(50)
items.insert(120)
items.insert(89)
items.insert(90)
items.insert(30)

items.insert_at(4, 2)
items.insert_at(6, 0)
items.insert_at(6, 9)
items.insert_at(56, 120)
items.print()
