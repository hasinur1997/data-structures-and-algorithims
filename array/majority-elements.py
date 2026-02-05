def get_majority(nums):
    nums.sort()
    return nums[len(nums) // 2]# Example usage:


def get_majority_count(nums):
    candidate = 0
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        
        count += (1 if num == candidate else -1)

    return candidate


numbers = [2,2,1,1,1,2,2]
print(get_majority(numbers))