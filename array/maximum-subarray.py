def get_max_sub_array(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        # current_sum *= nums[i]

        current_sum = max(nums[i], nums[i] * current_sum)
        max_sum = max(current_sum, max_sum)

    return max_sum




def binary_search(items, target):
    left, right = 0, len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid

        if items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def get_first_position(nums, target):
    left, right = 0, len(nums) - 1
    first = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            first =  mid
            right = mid - 1

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first


def get_last_position(nums, target):
    left, right = 0, len(nums) - 1
    last = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            last =  mid
            left = mid + 1

        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return last
