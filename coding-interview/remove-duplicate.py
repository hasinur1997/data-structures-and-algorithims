
def remove_duplicates(nums):
    n = len(nums)

    current_index = 1

    for i in range(1, n):

        if nums[i] != nums[i-1]:
            nums[current_index] = nums[i]
            current_index += 1

    return nums


numbers = [1, 1, 2, 2, 3, 3, 4, 4]

print(remove_duplicates(numbers))