numbers = [23, 45, 60, 120, 560, 790]

def print_array(data, index=0):
    if index >= len(data):
        return
    print(data[index])

    print_array(data, index+1)

def summation_of_array(data, index=0):
    if index >= len(data):
        return 0

    return data[index] + summation_of_array(data, index+1)

def get_even(data, index=0, even = []):
    if index >= len(data):
        return even

    if data[index] % 2 == 0:
        even.append(data[index])

    return get_even(data, index+1, even)


def print_n(n):
    if n < 0:
        return 0
    print(n)
    return n + print_n(n-1)


def factorial(n):
    if n < 1:
        return 1

    return n * factorial(n-1)




print(print_n(100))
