class Solution:
    def reverse(self, x):
        result = 0
        sign = -1 if x < 0 else 1
        number = abs(x)

        while number != 0:
            digit = number % 10
            result = result * 10 + digit
            number //= 10
        
        result *= sign
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result