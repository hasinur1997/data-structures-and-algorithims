def cell_with_odd_values(m, n, indices):
    numbers = [[0 for k in range(n)] for j in range(m)]
    odd = 0

    for i in range(len(indices)):
        r = indices[i][0]
        c = indices[i][1]

        for j in range(len(numbers[r])):
            numbers[r][j] += 1

        for k in range(len(numbers)):
            numbers[k][c] += 1

    for p in range(len(numbers)):
        for q in range(len(numbers[p])):
            if numbers[p][q] % 2 == 1:
                odd += 1

    return odd


m = 2
n = 2
indices = [[1,1],[0,0]]

# print(cell_with_odd_values(m, n, indices))


numbers = 1245

num = str(numbers)

print(num.split())

