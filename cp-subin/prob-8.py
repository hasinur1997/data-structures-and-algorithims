T = int(input())

index = 1

while index <= T:
    a = int(input())
    b = int(input())
    c = int(input())

    minimum = a
    if b < minimum:
        minimum = b
    if c < minimum:
        minimum = c

    # Find the maximum number
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c

    # Find the middle number
    middle = a + b + c - minimum - maximum

    print(f"Case {index}: {minimum} {middle} {maximum}")

    index += 1


