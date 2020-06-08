def arrayPairSum(nums):
    nums.sort()

    n = 0
    for i in range(len(nums)):
        if i%2 == 0:
            n += nums[i]
    return n

print(arrayPairSum([1,4,3,2]))