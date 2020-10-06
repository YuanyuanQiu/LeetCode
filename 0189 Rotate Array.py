def rotate(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[n-k:] + nums[:n-k]
    return nums

print(rotate([1,3,5,7], 3))