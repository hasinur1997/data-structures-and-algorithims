def max_water(height):
    result = 0
    l, r = 0, len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        result = max(area, result)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return result


height = [1,8,6,2,5,4,8,3,7]

result = max_water(height)
print(result)
