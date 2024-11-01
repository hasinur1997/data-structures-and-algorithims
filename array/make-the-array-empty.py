import heapq
def make_empty_array(nums):
    operations = 0
    heapq.heapify(nums)

    smallest = heapq.heappop(nums)

    while nums:
        smallest = min(nums)

        if nums[0] == smallest:
            nums.pop(0)
        else:
            nums.append(nums.pop(0))
        operations += 1

    return operations


nums = [1,2,4,3]

print(make_empty_array(nums))