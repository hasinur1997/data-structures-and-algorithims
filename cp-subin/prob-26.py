T = int(input())

while T > 0:
    count_days = 0
    X = float(input())

    while X >= 1:
        X = X / 2
        count_days += 1

    print(f"{count_days} days")

    T -= 1


