import random


class RandomizedSet:

    def __init__(self):
        self.data = {}

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False

        self.data[val] = val

        return True

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False

        del self.data[val]

        return True

    def getRandom(self) -> int:
        return random.choice(list(self.data.values()))





rd = RandomizedSet()
print(rd.insert(1))
print(rd.remove(2))
print(rd.insert(2))
print(rd.remove(1))
print(rd.getRandom())
