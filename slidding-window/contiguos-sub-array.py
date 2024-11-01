def get_windows(nums, k):
    current_sum = 0

    for i in range(k):
        current_sum += nums[i]

    max_sum = current_sum

    for i in range(k, len(nums)):
        current_sum = current_sum - nums[i-k] + nums[i]

        max_sum = max(max_sum, current_sum)

    return max_sum / k


items = [5]

result = get_windows(items, 1)
print(result)
