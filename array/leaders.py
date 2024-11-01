def get_leaders(arr):
    n = len(arr)
    max_from_right = arr[n-1]
    leaders = [max_from_right]

    for i in range(n - 2, -1, -1):
        if max_from_right < arr[i]:
            leaders.append(arr[i])
            max_from_right = arr[i]

    return leaders

arr = [16, 17, 4, 3, 5, 2]
print(get_leaders(arr))
