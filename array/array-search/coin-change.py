def coinChange(coins):
    if not coins:
        return 1

    coins.pop()

    return sum(coins) + 1


# coins = []
# print(coinChange(coins))
#
# coins = [1, 2, 5]
# print(coinChange(coins))
#
# coins = [5, 7, 1, 1, 2, 3, 22]
# print(coinChange(coins))


def trippleSum(array, targetSum):

    array.sort()
    triplets = []

    for i in range(len(array) - 2):
        currentNumber = i
        left = i + 1
        right = len(array) - 1

        while left < right:
            first = array[currentNumber]
            second = array[left]
            third = array[right]

            currentSum = first + second + third

            if currentSum == targetSum:
                triplets.append([first, second, third])
                left += 1
                right -= 1

            elif currentSum < targetSum:
                left += 1

            elif currentSum > targetSum:
                right -= 1

    return triplets



def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    pairs = []
    smallestNum = float('inf')
    currentNum = float('inf')


    i = 0
    j = 0

    # minDifference = arrayOne[0] - arrayTwo[0]

    while i < len(arrayOne) and j < len(arrayTwo):
        first = arrayOne[i]
        second = arrayTwo[j]

        if first < second:
            currentNum = second - first
            i += 1
        elif second < first:
            currentNum = first - second
            j += 1
        else:
            return [first, second]

        if smallestNum > currentNum:
            smallestNum = currentNum
            pairs = [first, second]

    return pairs


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

result = smallestDifference(arrayOne, arrayTwo)

print(result)
