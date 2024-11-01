def count_digit(number):
    if number < 10:
        return 1
    return 1 + count_digit(number//10)


print(count_digit(10456))

"""
1 -> count_digit(1045)
    1045 < 10: false
    
    return 1 + count_digit(104)
    
2 -> count_digit(104):
    104 < 10: false
    
    return 1 + count_digit(10)
    
3 -> count_digit(10)
    10 < 10: false
    
    return 1 + count_digit(1)
    

4  -> count_digit(1):
    1 < 10: True
        return 1

"""
