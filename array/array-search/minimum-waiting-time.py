from collections import Counter

def minimum_waiting_time(queries):
    queries.sort()
    currentWaitingTime = 0
    minimumSum = 0

    for i in range(1, len(queries)):

        currentWaitingTime += queries[i-1]
        minimumSum += currentWaitingTime

    return minimumSum


queries = [3, 2, 1, 2, 6]
result = minimum_waiting_time(queries)

# print(result)

def firstOccourance(array):
    countItems = {}

    for num in array:
        if num not in countItems:
            countItems[num] = 1
        else:
            countItems[num] += 1

        if countItems[num] > 1:
            return num

    return -1


def arrayProduct(array):
    result = [None for _ in range(len(array))]
    for i in range(len(array)):
        product = 1

        for j in range(len(array)):
            if i != j:
                product *= array[j]

        result[i] = product

    return result



def missingNumbers(nums):
    n_sum = 0
    s = set([0])

    for num in nums:

        n_sum += num
        print(s)
        if n_sum in s:
            return True
        s.add(n_sum)

    return False


items = [-5,-5,2,3,-2]
answer = missingNumbers(items)
# print(answer)

