def get_min(items):
    # items = sorted(items)
    #
    # return items[0]

    _min = items[0]

    for item in items:
        if item < _min:
            _min = item

    return _min



def get_max(items):

    # items = sorted(items, reverse=True)
    #
    # return items[0]

    _max = items[0]

    for item in items:
        if item > _max:
            _max = item

    return _max

items = [1, 423, 6, 46, 34, 23, 13, 53, 4]
_max = get_max(items)
_min = get_min(items)

print(_max, _min)
