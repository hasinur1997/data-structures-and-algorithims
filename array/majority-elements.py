def get_majority(nums):
    counter = {}
    n = len(nums) / 2

    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

        if counter[num] > n:
            return num


numbers = [2,2,1,1,1,2,2]
print(get_majority(numbers))