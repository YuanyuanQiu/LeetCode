class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = list(range(1,10))
        res = []
        def backtrack(i, temp_sum, temp_list):
            if temp_sum==n and len(temp_list)==k:
                res.append(temp_list)
                return
            
            if len(temp_list)==k:
                return

            for j in range(i, len(candidates)):
                if len(temp_list)==k-1:
                    if temp_sum+candidates[j]>n or temp_sum+candidates[-1]<n: # 稍微优化了一下
                        break
                backtrack(j+1, temp_sum+candidates[j], temp_list+[candidates[j]])
        backtrack(0,0,[])
        return res