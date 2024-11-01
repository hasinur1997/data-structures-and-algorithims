def reverse_string(s, n=0):
    if n > len(s) - 1:
        return

    reverse_string(s, n+1)
    print(s[n])

reverse_string("Hello World")
