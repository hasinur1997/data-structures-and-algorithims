def calcSubset(A, res, subset, index):

    res.append(subset[:])

    for i in range(index,  len(A)):
        subset.append(A[i])
        calcSubset(A, res, subset, i + 1)

        subset.pop()


def subsets(A):
    subset = []
    res = []
    index = 0
    calcSubset(A, res, subset, index)

    return res


array = [1, 2, 3]

res = subsets(array)

for subset in res:
    print(*subset)

