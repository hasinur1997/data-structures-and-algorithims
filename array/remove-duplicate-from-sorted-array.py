def remove_duplicate(nums):
    i = 0

    for j in range(len(nums)):

        if nums[i] == nums[j]:
            continue

        i += 1
        nums[i] = nums[j]

    return i + 1