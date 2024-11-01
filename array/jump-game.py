def jump_game(nums):

    for i, num in enumerate(nums):
        sub = nums[i+1:num]

        print(sub)


nums = [2,3,1,1,4]

jump_game(nums)