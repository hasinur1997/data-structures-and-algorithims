def prefix_sum(nums):

    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]

    return nums



nums = [10, 20, 10, 5, 15]
# print(prefix_sum(nums))

def product_except_self(items):
    n = len(items)
    prefix = [1] * n
    suffix = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i-1] * items[i-1]

    for k in range(n-2, -1, -1):
        suffix[k] = suffix[k+1] * items[k+1]

    for j in range(n):
        items[j] = prefix[j] * suffix[j]

    return items


items = [1,2,3,4]
results = product_except_self(items)

# print(results)

def valid_triplex(items):
    first = float('inf')
    second = float('inf')

    for num in items:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True

    return False


items = [20,100,10,12,5,13]

result = valid_triplex(items)
print(result)