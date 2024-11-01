def array_sum(numbers, index=0):
    try:
        return numbers[index] + array_sum(numbers, index+1)
    except:
        return 0



print(array_sum([10, 30, 40]))
