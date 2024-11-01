from collections import Counter


def can_construct(a, b):
    note = Counter(a)
    magazine = Counter(b)

    if len(magazine) < len(note):
        return False

    for key in note:
        if key not in magazine:
            return False

        if magazine[key] < note[key]:
            return False

    return True

note = "aa"
magazine = "aab"

print(can_construct(note, magazine))
