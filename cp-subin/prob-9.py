import math
T = int(input())

while T > 0:
    N = int(input())

    sq = int(math.sqrt(N))

    if sq ** 2 == N:
        print("YES")
    else:
        print("NO")

    T -= 1

