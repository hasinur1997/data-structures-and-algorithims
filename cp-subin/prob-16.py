T = int(input())

while T > 0:
    S = input()
    reverse = ''
    words = S.split()
    words  = [word[::-1] for word in words]

    print(' '.join(words))

    T -= 1