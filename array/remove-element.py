def remove_element(nums, val):
   j = 0

   for i in range(len(nums)):
      if nums[i] != val:
         nums[j] = nums[i]
         j += 1

   return j


nums = [3,2,2,3]
val = 3
print(remove_element(nums, val))

"""
   nums[0] == 2 // False
   nums[1] == 2 // False
"""