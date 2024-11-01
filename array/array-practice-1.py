from collections import Counter


def linear_search(array, search_key):
    for i, val in enumerate(array):
        if search_key == val:
            return i

    return -1


def binary_search(array, search_key):
    left = 0
    right = len(array) - 1
    array = sorted(array)

    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == search_key:
            return mid

        if array[mid] < search_key:
            left = mid + 1

        else:
            right = mid - 1

    return -1


def array_leaders(array):
    n = len(array) - 1
    leaders = [array[n]]

    for i in range(n-1, -1, -1):
        if array[i] >= array[i-1]:
            leaders.append(array[i])

    return leaders


def calculate_percentage(array):
    total = len(array)
    counter = dict(Counter(array))

    percentage = {}

    for item in counter:
        percentage[item] = (counter[item] / total) * 100

    return percentage


def array_modify(array):
    print(array)

    return array


items = [8, 9, 7, 0, 7, 5]
result = calculate_percentage(items)
print(result)



print(33.33333333333333 + 66.66666666666666)