class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def backtrack(i, used):
            ans.append(used)
            for j in range(i,n):
                backtrack(j+1, used + [nums[j]])    
        backtrack(0,[])  
        return ans