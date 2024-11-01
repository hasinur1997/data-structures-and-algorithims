def find_index(haystack, needle):
    if needle not in haystack:
        return -1

    return haystack.index(needle)


has = "sadbutsad"
needle = "sad"

print(find_index(has, needle))
