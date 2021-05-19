# dynamic programming
def lengthOfLIS(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 1
    # dp[i]: till nums[i] longest subsequence
    dp = [1 for _ in range(n)]
    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)