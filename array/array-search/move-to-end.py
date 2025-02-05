def move_to_end(array, toMove):
    i = 0
    j = len(array) - 1

    while i < j:

        while i < j and array[j] == toMove:
            j -= 1

        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]

        i += 1

    return array



def is_monotonic(array):

    return sorted(array) == array or sorted(array, reverse=True) == array


array = [4, 5, 6, 7, 8]
print(is_monotonic(array))

