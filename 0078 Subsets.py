class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        # 长度，已使用，剩余
        def backtrack(lens, used, remain):
            if len(used) == lens:
                ans.append(used)
                return
            if not remain:
                return
            for j in range(len(remain)):
                backtrack(lens, used + [remain[j]], remain[j+1:])
        
        for lens in range(n+1):   
            backtrack(lens,[],nums)
        
        return ans