def is_prime(number):
    if number == 0 or number == 1:
        return False

    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            return False

    return True

T = int(input())

while T > 0:
    a = int(input())
    b = int(input())
    counter = 0

    for i in range(a, b+1):
        if is_prime(i):
            counter += 1

    print(counter)
    T -= 1