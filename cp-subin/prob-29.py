def is_digit(ch):
    return ord('0') <= ord(ch) <= ord('9')


def is_lower(ch):
    return ord('a') <= ord(ch) <= ord('z')


def is_upper(ch):
    return ord('A') <= ord(ch) <= ord('Z')


T = int(input())

while T > 0:
    c = input()

    if is_lower(c):
        print("Lowercase Character")
    elif is_upper(c):
        print("Uppercase Character")
    elif is_digit(c):
        print("Numerical Digit")
    else:
        print("Special Character")

    T -= 1