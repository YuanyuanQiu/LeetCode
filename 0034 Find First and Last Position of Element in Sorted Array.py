def searchRange(nums, target):
    l = 0
    r = len(nums)-1
    flagl = 0
    flagr = 0
    while l <= r:
        # print(l,r,flagl,flagr)
        if flagl == 0:
            if nums[l] < target:
                l += 1
            elif nums[l] > target:
                return [-1, -1]
            else:
                flagl = 1
        if flagr == 0:
            if nums[r] > target:
                r -= 1
            elif nums[r] < target:
                return [-1, -1]
            else:
                flagr = 1
        if flagl + flagr == 2:
            break
    
    if flagl == 0 and flagr == 0:
        return [-1, -1]
    else:
        return [l,r]

print(searchRange([1], 1))