def findNumberOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 1

    dp = [1] * n # dp[i]：到nums[i]为止的最长递增子序列长度
    count = [1] * n # count[i]：到nums[i]为止的最长递增子序列个数
    max_length = 0
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]: # 遍历所有之前dp，若可增加num[i]
                if dp[j] + 1 > dp[i]: # 说明长度增加，数量不变
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                elif dp[j] + 1 == dp[i]: # 说明长度一样，数量增加
                    count[i] += count[j]
        max_length = max(max_length, dp[i])

    res = 0
    for i in range(n):
        if dp[i] == max_length:
            res += count[i]
    return res