def compress_string(chars):
    i = 0
    index = 0
    n = len(chars)
    while i < n:
        count = 0
        currentChar = chars[i]

        while i < n and chars[i] == currentChar:
            i += 1
            count += 1

        chars[index] = currentChar
        index += 1

        if count != 1:
            counters = list(str(count))
            for k in range(len(counters)):
                chars[index] = counters[k]
                index += 1

    return index

chars = ["a","a","b","b","c","c","c"]
compress_string(chars)

def consecutive(arr):

    for i in range(len(arr) - 2):
        if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
            return True

    return False


arr = [1, 3, 2]

result = consecutive(arr)
print(result)