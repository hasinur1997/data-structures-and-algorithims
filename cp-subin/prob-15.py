T = int(input())

while T > 0:
    S = input()
    count_character = {}

    for c in S:
        if c in count_character:
            count_character[c] += 1
        else:
            count_character[c] = 1

    sorted_dict = dict(sorted(count_character.items()))

    for ch, val in sorted_dict.items():
        print(f"{ch} = {val}")

    T -= 1

