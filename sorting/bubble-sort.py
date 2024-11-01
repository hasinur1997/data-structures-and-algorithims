def bubble_sort(items):
    n = len(items)
    counter = 0
    for i in range(n):
        for j in range(n):
            counter += 1
            if items[i] < items[j]:
                temp = items[i]
                items[i] = items[j]
                items[j] = temp

    return items


nums = [10, 3, 29, 34, 1, 0, 9, 54, 10]
print(bubble_sort(nums))
