def array_sum(items, n=0):
    if n > len(items) - 1:
        return 0

    return items[n] + array_sum(items, n+1)

print(array_sum([1, 2, 3]))
