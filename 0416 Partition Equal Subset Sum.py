def canPartition(self, nums: List[int]) -> bool:
    n = len(nums)
    if n < 2:
        return False
    
    total = sum(nums)
    maxNum = max(nums)
    # 奇数
    if total % 2 != 0:
        return False
    
    target = total // 2
    if maxNum > target:
        return False
    
    # dp[i][j]: 从数组的 [0,i]下标范围内选取若干个正整数（可以是0个）
    # 是否存在一种选取方案使得被选取的正整数的和等于j
    dp = [[False for _ in range(target + 1)] for _ in range(n)]
    
    # 如果不选取任何正整数，则被选取的正整数等于 00
    for i in range(n):
        dp[i][0] = True
    
    # 当 i==0时，只有一个正整数nums[0]可以被选取
    dp[0][nums[0]] = True
    for i in range(1, n):
        num = nums[i]
        for j in range(1, target + 1):
            # 对当前数字num可选可不选，一个为true则true
            if j >= num:
                dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
            # 无法选取当前数字
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n - 1][target]