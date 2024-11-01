def max_vowels(s, k):

    ans = 0
    count = 0
    vowels = 'aeiou'

    for i in range(len(s)):
        if i >= k:
            if s[i-k] in vowels:
                count -= 1

        if s[i] in vowels:
            count += 1

        ans = max(ans, count)

    return ans



input = 'abciiidef'
k = 3
result = max_vowels(input, k)
print(result)

