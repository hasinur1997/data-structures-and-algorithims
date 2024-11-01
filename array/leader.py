def printLeaders(arr):
    n = len(arr)
    max_from_right = arr[n-1]
    t = [max_from_right]

    for i in range(n-2, -1, -1):
        if max_from_right < arr[i]:
            t.append(arr[i])
            max_from_right = arr[i]

    return t

print(printLeaders([16, 17, 4, 3, 5, 2]))

