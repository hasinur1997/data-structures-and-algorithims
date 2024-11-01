def isPairSum(items, x):
    i = 0
    j = len(items) - 1

    pairs = []

    while i < j:
        if items[i] == x:
            return True

        elif items[i] < x:
            i += 1
        else:
            j -= 1

    return False



def merge_two_sorted_array(array1, array2):
    new_array = []

    i = 0
    j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            new_array.append(array1[i])
            i += 1
        else:
            new_array.append(array2[j])
            j +=1


    while i < len(array1):
        new_array.append(array1[i])
        i += 1


    while j < len(array2):
        new_array.append(array2[j])
        j += 1


    return new_array




a = [1, 2, 3, 4, 5]
a2 = [0, 3,4, 4, 6, 7, 8, 9]
result = merge_two_sorted_array(a, a2)
print(result)

def is_palindrome(items):
    i = 0
    j = len(items) - 1

    while i < j:
        if items[i] != items[j]:
            return False

        i += 1
        j -= 1

    return True


items = [1, 2, 1]
result = is_palindrome(items)

print(result)

def merge_string(a, b):
    i = 0
    j = 0
    new_string = ''

    n1 = len(a)
    n2 = len(b)

    while i < n1 and j < n2:
        new_string += a[i]
        new_string += b[j]

        i += 1
        j += 1

    while i < n1:
        new_string += a[i]
        i +=1

    while j < n2:
        new_string += b[j]
        j += 1

    return new_string


def gcd_string(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""

    i = 0
    j = 0

    result = ''

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j] and str1[i] not in result:
            result += str1[i]

        i += 1
        j += 1

    return result

result = gcd_string('LEET', 'CODE')
print(result)