def get_fact(number):
    if number <= 0:
        return 1
    return number * get_fact(number - 1)


def count_zero(number):
    counter = 0

    while number > 0:
        reminder = number % 10
        number = number // 10
        if reminder != 0:
            break
        counter += 1

    return counter


T = int(input())

while T > 0:
    N = int(input())

    print(count_zero(get_fact(N)))

    T -= 1

