class MyHashSet:
    def __init__(self):
        self.size = 2
        self.data = [None] * self.size

    def add(self, key: int) -> None:
        index = self._hash(key)

        if self.data[index] is None:
            self.data[index] = [(key, True)]
        else:
            for i, (existing_key, _) in enumerate(self.data[index]):
                if key == existing_key:
                    self.data[index][i] = (key, True)
                    break
            else:
                self.data[index].append((key, True))

    def remove(self, key: int) -> None:
        index = self._hash(key)

        if self.data[index] is not None:
            for i, (existing_key, _) in enumerate(self.data[index]):
                if existing_key == key:
                    del self.data[index][i]
                    break

    def contains(self, key: int) -> bool:
        index = self._hash(key)

        if self.data[index] is not None:
            for i, (existing_key, _) in enumerate(self.data[index]):
                if key == existing_key:
                    return True

        return False

    def _hash(self, key):
        return hash(key) % self.size


myset = MyHashSet()
myset.add(1)
myset.add(2)
print(myset.data)
print(myset.contains(1))
print(myset.contains(3))
myset.add(2)
print(myset.contains(2))
myset.remove(2)
print(myset.contains(2))

# print(hash(3495734957934750734905) % 10)

