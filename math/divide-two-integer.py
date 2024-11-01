def divide(dividend: int, divisor: int) -> int:
    counter = 0
    x = divisor
    y = dividend
    if dividend < 0:
        dividend = dividend * -1

    if divisor < 0:
        divisor = divisor * -1

    while dividend >= divisor:
        dividend -= divisor
        counter += 1


    if x < 0 or y < 0:
        counter = counter * -1

    return counter


dividend = -1
divisor = -1
print(divide(dividend, divisor))

print(-1 / -1)