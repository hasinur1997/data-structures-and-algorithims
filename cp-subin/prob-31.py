def perfect_number(number):
    if number <= 0:
        return False

    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    return divisors_sum == number


T = int(input())

while T > 0:
    N = int(input())

    for i in range(1, N+1):
        if perfect_number(i):
            print(i)
    print()
    T -= 1


