def is_strict_palindromic(n):
    for i in range(2, n-1):
        if not is_palindromic(n, i):
            return False

    return True


def is_palindromic(n, base):
    binary = decimal_bn(n, base)

    left = 0
    right = len(binary) - 1

    while left < right:
        if binary[left] != binary[right]:
            return False

        left += 1
        right -= 1

    return True


def decimal_bn(number, base):
    binary = []

    while number > 0:
        binary.insert(0, str(number % base))
        number //= base

    return ''.join(binary)


number = 10
print(is_strict_palindromic(number))
