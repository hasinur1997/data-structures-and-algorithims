
T = int(input())

while T > 0:
    string = input()
    character = input()

    counter = string.count(character)

    if counter > 0:
        print(f"Occurrence of '{character}' in 'hello world' = {counter}")
    else:
        print(f"'{character}' is not present")

    T -= 1

