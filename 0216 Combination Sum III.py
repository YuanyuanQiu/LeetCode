class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ls = list(range(1,10))
        res = []
        def dfs(history, remain, n):
            if len(history) == k:
                if sum(history) == n:
                    res.append(history)
                else:
                    return
            if not remain:
                return
            for i in range(len(remain)):
                dfs(history + [remain[i]], remain[i+1:], n)
        
        dfs([], ls, n)
        return res