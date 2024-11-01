def reverse(items):
    i = 0
    j = len(items) - 1
    while i < j:
        items[i], items[j] = items[j], items[i]
        i += 1
        j -= 1

    return items


def recur_revers(items, start, end):
    if start >= end:
        return items

    items[start], items[end] = items[end], items[start]

    return recur_revers(items, start+1, end-1)

items = [1, 2, 3]

print(recur_revers(items, 0, len(items)-1))
