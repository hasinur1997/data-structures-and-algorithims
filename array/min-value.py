def get_min_value(items):
    if not items:
        return False

    min_value = items[0]

    for item in items:
        if item < min_value:
            min_value = item

    return min_value


# numbers = [3, 59, 10, 230, 50, 2]
#
# print(get_min_value(numbers))

def move_to_zeros(items):
    if not items:
        return False

    j = 0
    for i in range(len(items)):
        if items[i] != 0 and items[j] == 0:
            temp = items[i]
            items[i] = items[j]
            items[j] = temp

        if items[j] != 0:
            j += 1

    return items


numbers = [0, 3, 0, 59, 10, 0, 230, 50, 2]

print(move_to_zeros(numbers))


