def maximum_string_pairs(words):
    word_dict = {}
    max_pairs = 0

    for word in words:
        revers_word = word[::-1]

        if word in word_dict:
            word_dict[word] += 1
        elif revers_word in word_dict:
            word_dict[revers_word] += 1
        else:
            word_dict[word] = 1

    for key in word_dict:
        pair = word_dict[key] // 2
        if pair > 0:
            max_pairs += pair

    return max_pairs


words = ["aa","ab"]
print(maximum_string_pairs(words))
