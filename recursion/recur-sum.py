def recur_sum(n):
    if n < 1:
        return 0
    return n + recur_sum(n-1)


print(recur_sum(10))

"""
   1 ->  recur_sum(10)
        10 < 1: false
    param = 10 - 1 = 9
    return 10 + recur_sum(9)
    
    2 -> recur_sum(9)
        9 < 1: false
    param = 9 - 1 = 8
    return 9 + recur_sum(8)
    
    3 -> recur_sum(8)
        8 < 1: false
    return 8 + recur_sum(7)
    
    4 -> recur_sum(7)
        7 < 1: false
    return 7 + recur_sum(6)
    
    5 -> recur_sum(6)
        6 < 1: false
    return 6 + recur_sum(5)
    
    6 -> recur_sum(5)
        5 < 1: false
    return 5 + recur_sum(4)
    
    7 -> recur_sum(4)
        4 < 1: false
    return 6 + recur_sum(3)
    
    8 -> recur_sum(3)
        3 < 1: false
    return 3 + recur_sum(2)
    
    9 -> recur_sum(2)
        2 < 1: false
    return 2 + recur_sum(1)
    
    10 -> recur_sum(1)
        1 < 1: false
    return 1 + recur_sum(0)
    
    11 -> recur_sum(0)
        0 < 1: false
            return 0
    return 0 + recur_sum(0)
"""