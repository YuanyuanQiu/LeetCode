# backtracking
def combinationSum4(self, nums: List[int], target: int) -> int:
    if not nums:
        return 0
    nums = sorted(nums)
    res = []
    
    def backtrack(i, temp_sum, temp_list):
        if temp_sum == target:
            res.append(temp_list)
            return

        if temp_sum > target:
            return

        for j in range(len(nums)):
            backtrack(j, temp_sum + nums[j], temp_list + [nums[j]])

    backtrack(0,0,[])
    return len(res)
    
# dynamic programming
def combinationSum4(self, nums, target):
    if not nums or target < min(nums):
        return 0
    dp = [0 for _ in range(target + 1)]
    # 只有当不选取任何元素时，元素之和才为0，因此只有1种方案。
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i-num]
    return dp[-1]