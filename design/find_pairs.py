class FindSumPairs:

    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

        self.nums2 = sorted(self.nums2)

    def count(self, tot: int) -> int:
        counter = 0

        for num in self.nums2:
            value = tot - num

            if value in self.nums1:
                counter += 1
        return counter





pair = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])

print(pair.count(7))
pair.add(3, 2)
print(pair.count(8))
print(pair.count(4))
print(pair.add(0, 1))
print(pair.add(1, 1))
print(pair.count(7))

print(pair.nums1)
print(pair.nums2)
# test1 = [1, 3, 4, 5, 5]
# test2 = [3, 4, 1, 5, 5, 7, 6]
# test1[0] += 2
# target = 10
#
# counter = 0
#
# for num in test1:
#     value = target - num
#
#     if value in test2:
#         counter += 1
#
# print(counter)
