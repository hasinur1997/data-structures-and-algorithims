def missing_positive_int(nums):
    nums_set, i = set(nums), 1
    while i in nums_set:
        i += 1
    return i

numbers = [7,8,9,11,12]
print(missing_positive_int(numbers))
