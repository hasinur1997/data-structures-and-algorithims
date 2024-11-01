def rearrange(items, key):
    j = 0
    i = 0
    n  = len(items)

    while i < n:
        if items[i] <= key:
            items[i], items[j] = items[j], items[i]
            j += 1
        i += 1

    return items

items = [-1, 2, -3, 4, 5, 6, -7, 8, 9]

print(rearrange(items, 5))