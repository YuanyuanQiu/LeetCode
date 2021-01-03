# backtracking
class Solution:
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
class Solution:
    def combinationSum4(self, nums, target):
        size = len(nums)
        if size == 0 or target <= 0:
            return 0

        dp = [0 for _ in range(target + 1)]
        
        # 这一步很关键，想想为什么 dp[0] 是 1
        # 因为 0 表示空集，空集和它"前面"的元素凑成一种解法，所以是 1
        # 这个值被其它状态参考，设置为 1 是合理的
        
        dp[0] = 1

        for i in range(1, target + 1):
            for j in range(size):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]

        return dp[-1]