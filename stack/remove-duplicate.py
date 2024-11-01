def removeDuplicates(s: str) -> str:
    lis = [s[0]]

    for i in range(1, len(s)):
        n = len(lis)

        if n == 0 or lis[n-1] != s[i]:
            lis.append(s[i])
        else:
            lis = lis[:n-1]

    return ''.join(lis)



st = 'axxyzzf'
print(removeDuplicates(st))


test = 'abcdedfg'

print(test[:len(test)-1])
