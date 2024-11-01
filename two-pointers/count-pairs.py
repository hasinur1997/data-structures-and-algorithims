def count_pairs(nums, k):
    count = 0
    num_dict = {}

    for num in nums:
        complement = k - num
        if num_dict.get(complement, 0) > 0:
            count += 1
            num_dict[complement] -= 1
        else:
            num_dict[num] = num_dict.get(num, 0) + 1

    return count


nums = [1,2,3,4]
k = 5

result = count_pairs(nums, k)
print(result)
