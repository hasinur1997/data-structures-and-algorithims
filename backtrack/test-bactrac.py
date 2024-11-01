def toString(List):
    # return ''.join(List)
    return ''.join(List)

def permute(a, l, r):
    permutations = []
    if l == r:
        permutations.append(toString(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permutations.extend(permute(a, l+1, r))
            a[l], a[i] = a[i], a[l]  # backtrack
    return permutations

# Driver code
string = 'ABC'
n = len(string)
a = list(string)
result = permute(a, 0, n)
print(result)
