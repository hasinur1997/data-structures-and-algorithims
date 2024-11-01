def countDigits(num: int) -> int:
    x = num

    counter = 0

    while x > 0:
        mode = x % 10
        if num % mode == 0:
            counter += 1

        x //= 10
    return counter


num = 121
print(countDigits(num))
