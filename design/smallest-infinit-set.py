class SmallestInfiniteSet:

    def __init__(self):
        self.nums = set([i for i in range(1000, 0, -1)])

    def popSmallest(self) -> int:
        pass
    def addBack(self, num: int) -> None:
        pass


infinit = SmallestInfiniteSet()

print(infinit.nums)

test = set([1, 4, 5])

test.add(0)

nums = list(test)

print(nums.pop(0))
test.add(0)
print(nums.pop(0))
print(nums)
