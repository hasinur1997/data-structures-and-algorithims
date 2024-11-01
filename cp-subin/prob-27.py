
def count_digit(number):
    counter = 0

    while number > 0:
        number //= 10
        counter += 1

    return counter


def get_sum(number):
    summation = 0
    total_digit = count_digit(number)

    while number > 0:
        reminder = number % 10
        summation += reminder ** total_digit
        number //= 10

    return summation


T = int(input())

while T > 0:
    n = int(input())
    summation = get_sum(n)

    if n == summation:
        print(f"{n} is an armstrong number!")
    else:
        print(f"{n} is not an armstrong number!")
    T -= 1
