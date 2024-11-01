def get_lcm(x, y):
    z = x
    if y > x:
        z = y

    while True:
        if z % x == 0 and z % y == 0:
            return z
        z += 1


T = int(input())

while T > 0:
    a = int(input())
    b = int(input())

    lcm = get_lcm(a, b)
    print(lcm)
    T -= 1
