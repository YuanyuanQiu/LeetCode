def fourSum(nums, target):
    n = len(nums)
    
    if n < 4:
        return []
    if n == 4:
        if sum(nums) == target:
            return [nums]
        else:
            return []
    
    nums.sort()
    # print(nums)
    res = []
    
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            l = j+1
            r = n-1
            while l<r:
                # print(i,j,l,r)
                if l > j+1 and nums[l] == nums[l-1]:
                    # print('pass')
                    l += 1
                    continue
                
                temp = nums[i] + nums[j] + nums[l] + nums[r]
                if temp == target:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    # print('add',[nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                elif temp < target:
                    l += 1
                else:
                    r -= 1
    
    return res

print(fourSum([-3,-2,-1,0,0,1,2,3], 0))








