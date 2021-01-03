class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        candidates.sort()
        res=[]
        def backtrack(i,temp_sum,temp_list):
            if temp_sum==target:
                res.append(temp_list)
                return        
            if temp_sum>target or i==len(candidates):
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:#和39题不一样的地方，主要是为了防止出现重复的解
                    continue            
                backtrack(j+1,temp_sum+candidates[j], temp_list+[candidates[j]])
        backtrack(0,0,[])
        return res