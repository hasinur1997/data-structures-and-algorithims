def merge(items1, items2):
    i = j = 0
    result = []
    n1 = len(items1)
    n2 = len(items2)

    while i < n1 and j < n2:
        if items1[i] > items2[j]:
            result.append(items2[j])

            j += 1
        else:
            result.append(items1[i])
            i += 1

    result.extend(items1[i:])
    result.extend(items2[j:])

    return result


def merge_sort(items):
    n = len(items)

    if n <= 1:
        return items

    mid = n // 2
    left = items[:mid]
    right = items[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


numbers = [0, -2, 23, 1, -9, 39, 40]

print(merge_sort(numbers))

