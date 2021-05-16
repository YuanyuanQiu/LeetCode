def combine(self, n: int, k: int) -> List[List[int]]:
    ls = list(range(1,n+1))
    res = []
    def dfs(history, remain):
        if len(history) == k:
            res.append(history)
        if not remain:
            return
        for i in range(len(remain)):
            dfs(history + [remain[i]], remain[i+1:])
    dfs([], ls)
    return res