def faulty_keyboard(s):
    new_str = ''

    for ch in s:
        if 'i' == ch:
            new_str = new_str[::-1]
        else:
            new_str += ch

    return new_str

test_str = 'poiinter'

print(faulty_keyboard(test_str))

