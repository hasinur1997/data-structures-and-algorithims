def find_missing_number(items):
    n = len(items) + 1
    summation = int(n * (n+1) / 2)

    for num in items:
        summation = summation - num

    return summation


numbers = [1, 2, 3, 5]

print(find_missing_number(numbers))

