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
            

def threeSumClosest(self, nums: List[int], target: int) -> int:
    n = len(nums)
    nums.sort()
    res = sum(nums[:3])
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        l, r = i+1, n-1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if abs(total-target) < abs(res-target):
                res = total
            if total == target:
                return total
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif total > target:
                r -= 1
            else:
                l += 1
    return res   