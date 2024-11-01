def remove_duplicate(nums):
    j = 0

    for i in range(len(nums)):
        if nums[0:j].count(nums[i]) <= 1:
            nums[j] = nums[i]

            j += 1

    return j

    # print(nums)



numbers = [0,0,1,1,1,1,2,3,3]
print(remove_duplicate(numbers))