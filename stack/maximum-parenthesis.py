def maximum(s):
    stack = []
    maxi = 0
    for ch in s:
        if ch == '(':
            stack.append(ch)
            maxi = max(len(stack), maxi)
        elif ch == ')':
            stack.pop()

    return maxi


st = "(1+(2*3)+((8)/4))+1"
print(maximum(st))
