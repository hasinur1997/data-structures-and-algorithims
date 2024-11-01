def candy(ratings):
    minimum_candy = len(ratings)
    extra_candy = 0

    i = 0

    while i < len(ratings):
        left = i - 1
        right = i + 1

        if left == -1:
            left = 0

        if right > len(ratings) - 1:
            right = len(ratings) - 1

        if ratings[i] > ratings[left] or ratings[i] > ratings[right]:
            print(ratings[i])

        i += 1



ratings = [1,2,87,87,87,2,1]

"""
    candy = 7
    1
    
    
"""

print(candy(ratings))
