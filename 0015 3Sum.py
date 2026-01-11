class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    
                    # 1. 跳过左边重复的 (Skip duplicates from left)
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    # 2. 跳过右边重复的 (Skip duplicates from right)
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    
                    # 3. 关键一步：双指针必须同时向内收缩，寻找下一组
                    j += 1
                    k -= 1
                    
                elif total < 0:
                    j += 1
                else:
                    k -= 1
        return res