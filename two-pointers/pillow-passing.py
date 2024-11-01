def pillow_paas(n, time):
    i = 1

    while time > 0:
        while i < n and time > 0:
            i += 1
            time -= 1
        while i > 1 and time > 0:
            i -= 1
            time -= 1

    return i

result = pillow_paas(4, 5)

print(result)
