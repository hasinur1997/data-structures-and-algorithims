def findWinner(n, k):
    friends = list(range(1, n+1))
    currentIndex = 0

    while len(friends) > 1:

        currentIndex = (currentIndex + k - 1) % len(friends)

        friends.pop(currentIndex)

    return friends[0]


resutl = findWinner(5, 2)
print(resutl)
