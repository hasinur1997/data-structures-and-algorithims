def find_missing_number(nums):
    n = len(nums)
    total = (n + 1) * (n + 2) // 2

    return total - sum(nums)


nums = [1, 2, 4, 6, 3, 7, 8]
print(find_missing_number(nums))
