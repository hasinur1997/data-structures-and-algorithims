def count_pairs(nums, target):
    nums.sort()
    l = 0
    r = len(nums) - 1
    counter = 0

    while l < r:
        if nums[l] + nums[r] < target:
            counter += (r - l)
            l += 1
        else:
            r -= 1

    return counter



nums = [-6,2,5,-2,-7,-1,3]
target = -2

print(count_pairs(nums, target))

"""
    i = 0
    j = 1
    
    nums[0] = -1
    nums[1] = 1
    - 1 + 1 = 0; 0 < 2 = true
    
    i = 1
    j = 2
    
    nums[1] = 1
    nums[2] = 2
    
    1 + 2 = 3; 3 < 2 = false
    
    i = 2
    j = 3
    
    nums[2] = 2
    nums[3] = 3
    
    2 + 3 = 5; 5 < 2 = false
    
    i = 3
    j = 4
    
    3 + 1 = 4; 4 < 2 = false
"""