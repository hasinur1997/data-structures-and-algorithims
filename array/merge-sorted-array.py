def merge(nums1, m, nums2, n):
    for i in range(n):
        nums1[m] = nums2[i]
        m += 1
    nums1.sort()
    return nums1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

print(merge(nums1, m, nums2, n))