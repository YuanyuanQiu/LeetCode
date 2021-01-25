def canPartition(self, nums: List[int]) -> bool:
    n = len(nums)
    if n < 2:
        return False
    
    total = sum(nums)
    if total % 2 != 0:
        return False
    
    target = total // 2
    dp = [True] + [False] * target
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] |= dp[j - num]
        if dp[target]:
            break
    
    return dp[target]