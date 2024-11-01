def is_valid_palindrome(s):
    s = s.lower()


    ch = ''

    for k in range(len(s)):
        if s[k].isalnum():
            ch += s[k]

    print(ch)
    i = 0
    j = len(ch) - 1
    while i < j:
        if ch[i] != ch[j]:
            return False
        i += 1
        j -= 1

    return True


s = 'A man, a plan, a canal: Panama'

print(is_valid_palindrome(s))