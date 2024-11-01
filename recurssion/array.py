
def print_array(data, index=0):

    length = len(data)

    if index == length:
        return

    print(data[index])

    print_array(data, index+1)


data_set = [1, 3, 4, 5, 6, 7, 9, 51]

# print_array(data_set)


def get_odd(data, index=0):
    length = len(data)

    if index == length:
        return 0
    results = 0

    if data[index] % 2 != 0:
        results += data[index]

    return results + get_odd(data, index + 1)


print(get_odd(data_set))
