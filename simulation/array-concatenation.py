def array_concatenation(nums):
    total = 0
    left = 0
    right = len(nums) - 1

    while left <= right:
        # if left < right:
        #     total += int(str(nums[left]) + str(nums[right]))
        # else:
        #     total += nums[left]
        #
        # left += 1
        # right -= 1
        total += int(str(nums[left]) + str(nums[right]))
        left += 1
        right -= 1

    return total

nums = [7,52,2,4]

print(array_concatenation(nums))