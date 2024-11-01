from collections import Counter

class MajorityChecker:
    def __init__(self, arr):
        self.data = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        sub_arry = self.data[left:right+1]
        counter = Counter(sub_arry)

        for num in sub_arry:
            if counter[num] >= threshold:
                return num

        return -1

obj = MajorityChecker([1, 1, 2, 2, 1, 1])

print(obj.query(0, 5, 4))
print(obj.query(0, 3, 3))
print(obj.query(2, 3, 2))



