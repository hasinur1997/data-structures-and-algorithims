T = int(input())

while T > 0:
    S = input()
    v = ['a', 'e', 'i', 'o', 'u']

    vowel = ''
    con = ''

    for ch in S:
        if ch == ' ':
            continue
        if ch.lower() in v:
            vowel += ch
        else:
            con += ch

    print(vowel)
    print(con)

    T -= 1