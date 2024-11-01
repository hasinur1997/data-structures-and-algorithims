def is_valid(s):
    stack = []
    brackets = {'(': ')', '{': '}', '[': ']'}

    for ch in s:
        if ch in brackets:
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()

            if brackets[top] != ch:
                return False

    return len(stack) == 0

s = '()[]{'
print(is_valid(s))
