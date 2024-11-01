def quick_sort(nums):
    low = 0
    high = len(nums) - 1

    def partition(array, low, high):
        i = low
        j = low
        pivot = array[high]

        while i <= high:
            if array[i] <= pivot:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                j += 1

            i += 1

        return j - 1

    def quick_sort(array, low, high):

        if low < high:
            p = partition(array, low, high)

            quick_sort(array, low, p - 1)
            quick_sort(array, p + 1, high)

    quick_sort(nums, low, high)

    return nums


numbers = [-2, -5, 1, 6, 20, 3, 5, 103, 56]

print(quick_sort(numbers))
