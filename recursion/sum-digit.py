def sum_digit(numer):
    if numer < 1:
        return 0
    mod = numer % 10
    return mod + sum_digit(numer//10)


