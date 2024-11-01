def can_place_flowers(flowerbed, n):
    counter = 0
    neibours = {}

    for i in range(len(flowerbed)):
        current_plot = flowerbed[i]
        prev_plot = flowerbed[i - 1] if i > 0 else 0
        next_plot = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0

        # if current_plot not in neibours:
        neibours[i] = [prev_plot, next_plot]

    return neibours


flowerbed = [1,0,0,0,1]


def productExceptSelf(nums):
    result = 1
    for i in range(len(nums)):
        k = result * nums[i]
        if k > 0:
            result *= nums[i]

    for j in range(len(nums)):
        item = result // nums[j] if nums[j] > 0 else 0
        nums[j] = item
    print(result)
    return nums

items = [-1,1,0,-3,3]
print(productExceptSelf(items))
