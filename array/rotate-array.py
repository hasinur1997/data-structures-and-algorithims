def rotate_array(nums, k):
    n = len(nums) - 1
    for i in range(k):
        nums.insert(0, nums.pop())

    print(nums)


numbers = [1,2,3,4,5,6,7]
k = 3

rotate_array(numbers, k)
