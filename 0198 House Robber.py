# 动态规划
def rob(nums):
    # 边界条件
    if not nums:
        return 0
    size = len(nums)
    if size == 1:
        return nums[0]
    # dp[i-2], dp[i-1]滚动数组
    first, second = nums[0], max(nums[0], nums[1])
    
    # 转移方程 dp[i]=max(dp[i−2]+nums[i],dp[i−1])
    for i in range(2, size):
        first, second = second, max(first + nums[i], second)
    
    return second

print(rob([2,7,9,3,1]))