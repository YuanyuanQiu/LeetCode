def threeSum(nums):
    n = len(nums)
    if n < 3:
        return []
    nums.sort()
    res = []
    for i in range(n):
        if nums[i] > 0:
            return res
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = n - 1
        while l < r:
            val = nums[i] + nums[l] + nums[r]
            if val == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif val > 0:
                r -= 1
            else:
                l += 1       
    return res
