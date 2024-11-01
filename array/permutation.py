def permutation(nums):
    permutations = []

    for i in range(len(nums)):
        permutation = []
        for j in range(len(nums)):
           # permutation.append(nums[i])
            if nums[i] != nums[j]:
                permutations.append(nums[i])
            # else:
            #     permutation.append(nums[j])

        permutations.append(permutation)

    print(permutations)

nums = [1, 2, 3]

permutation(nums)
