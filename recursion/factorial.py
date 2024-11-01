def fact(number):
    if number < 1:
        return 1

    return number * fact(number - 1)

# print(fact(10))

def pow(n, x):
    result = 1
    for i in range(x):
        result *= n

    return result

print(pow(10, 2))