
T = int(input())

while T > 0:
    fact = 1
    N = int(input())

    for i in range(1, N+1):
        fact *= i

    print(fact)

    T -= 1