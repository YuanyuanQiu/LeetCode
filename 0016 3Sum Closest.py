def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    res = nums[0] + nums[1] + nums[2]

    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        l = i+1
        r = n-1

        while l < r:
            temp = nums[i] + nums[l] + nums[r]
            # print(i,l,r,res, temp)
            
            if abs(target - temp) < abs(target - res):
                res = temp
              
            if temp == target:
                return res
            elif temp > target:
                r -= 1
            else:
                l += 1
        
    return res
            
print(threeSumClosest([-100,-98,-2,-1], -101))       