T = int(input())

while T > 0:

    n = int(input())
    nums = []
    while n > 0:
        num = int(input())
        nums.append(num)
        n -= 1

    asending_sorted = sorted(nums)
    desending_sorted = sorted(nums, reverse=True)

    if asending_sorted == nums or desending_sorted == nums:
        print("YES")
    else:
        print("NO")
    T -= 1
