from collections import Counter

def is_permutation(s1, s2):
    counter1 = Counter(s1)
    counter2 = Counter(s2)

    return counter1 == counter2


def urlify(s):

    words = s.split()

    return '%20'.join(words)


print(urlify('   Mr.  Hasinur Rahman  '))