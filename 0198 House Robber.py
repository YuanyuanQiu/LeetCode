# Option 1 O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]
    
# Option 2 O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        pre2 = nums[0]
        pre1 = max(nums[0], nums[1])
        for i in range(2, n):
            cur = max(pre2 + nums[i], pre1)
            pre2 = pre1
            pre1 = cur
        return cur