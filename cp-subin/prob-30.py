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

    if perfect_number(N):
        print(f"YES, {N} is a perfect number!")
    else:
        print(f"NO, {N} is not a perfect number!")

    T -= 1


