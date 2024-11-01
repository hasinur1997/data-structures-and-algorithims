from collections import Counter


def count_hash_table(nums):
    items = Counter(nums)
    for i in range(len(nums)):
        print(items[i], nums[i])
        # if items[nums[i]] != nums[i]:
        #     return False
        # print(items['0'])
    return True

numbers = '1210'
print(count_hash_table(numbers))
