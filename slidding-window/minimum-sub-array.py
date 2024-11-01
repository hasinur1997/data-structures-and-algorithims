def sub_array(target, nums):
    sub_array_length = 0
    sub_array = 0
    nums = sorted(nums, reverse=True)
    # print(nums)
    for num in nums:
        if sub_array >= target:
            return sub_array_length
        sub_array += num
        sub_array_length += 1

    # print(sub_array)
    return 0



target = 213
nums = [12,28,83,4,25,26,25,2,25,25,25,12]



print(sub_array(target, nums))