def longest_substring(s):
    sub = ""
    max_lenght = 0

    for ch in s:
        if ch not in sub:
            sub += ch
        else:
            max_lenght = max(max_lenght, len(sub))
            sub = ch

    return max_lenght



s = " "

print(longest_substring(s))
