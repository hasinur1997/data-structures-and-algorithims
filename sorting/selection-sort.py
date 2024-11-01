def selection_sort(items):
    if not items:
        return

    n = len(items)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if items[min_index] > items[j]:
                min_index = j

        items[i], items[min_index] = items[min_index], items[i]

    return items


numbers = [2, 10, 38, 1, 4, 3, 5, 9]
print(selection_sort(numbers))
