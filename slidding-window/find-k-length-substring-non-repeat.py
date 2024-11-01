def find_k_length_substring(s, k):
    n = len(s)
    if n < k:
        return 0

    seen = set()
    count = 0
    start = 0

    for end in range(n):
        while s[end] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[end])

        if end - start + 1 == k:
            count += 1
            seen.remove(s[start])
            start += 1

    return count





s = 'abcabc'
k = 3

print(find_k_length_substring(s, k))
