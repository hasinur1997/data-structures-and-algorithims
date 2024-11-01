def two_sum(numbers, target):
    tracker = {}
    i = 0
    n = len(numbers)

    while i < n:
        result = target - numbers[i]
        if numbers[i] in tracker:
            return [tracker[numbers[i]], i+1]
        else:
            tracker[result] = i + 1

        i += 1

    return []


numbers = [2,3,4]
target = 6

print(two_sum(numbers, target))
