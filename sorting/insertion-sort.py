def insertion_sort(items):
    n = len(items)

    for i in range(1, n):

        item = items[i]

        j = i - 1

        while j >= 0 and items[j] > item:
            items[j+1] = items[j]
            j -= 1

        items[j+1] = item

    return items


numbers = [2, 10, 38, 1, 4, 3, 5, 9]
print(insertion_sort(numbers))
