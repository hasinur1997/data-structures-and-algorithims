def sum_of_squares(nums):
    i = 1
    n = len(nums)
    summation = 0

    for num in nums:
        if n % i == 0:
            summation += num * num
        i += 1

    return summation


nums = [2,7,1,19,18,3]
print(sum_of_squares(nums))
