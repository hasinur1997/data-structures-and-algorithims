def fibbo(n):
    if n <= 1:
        return 1

    return fibbo(n - 2) + fibbo(n - 1)

print(fibbo(3))