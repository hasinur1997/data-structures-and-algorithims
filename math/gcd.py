



def gcd(a, b):

    result = min(a, b)

    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1

    return result


result = gcd(78490, 2)

print(result)

s = 'ABABABAB'

print(s[0:2])