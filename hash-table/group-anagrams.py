def group_anagrams(strs):
    if not strs:
        return [[""]]
    counter = {}

    for item in strs:
        key = ''.join(sorted(item))

        if key in counter:
            counter[key].append(item)
        else:
            counter[key] = [item]

    return list(counter.values())


strs = ["eat","tea","tan","ate","nat","bat"]
strs = ""

print(group_anagrams(strs))
