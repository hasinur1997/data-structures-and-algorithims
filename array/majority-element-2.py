from collections import Counter


def majorityElement(nums):
    n = len(nums) / 3
    majority = []

    counter = Counter(nums)

    for num in nums:
        if counter[num] > n and num not in majority:
            majority.append(num)

    return majority


nums = [1, 2]
print(majorityElement(nums))
