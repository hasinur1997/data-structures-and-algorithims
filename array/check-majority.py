def isMajority(nums, x):
    n = len(nums)
    last_index = (n // 2 + 1) if n % 2 == 0 else (n // 2)

    for i in range(last_index):
        if nums[i] == x and nums[i + n//2] == x:
            return True

    return False
