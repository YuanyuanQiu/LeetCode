def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    if not candidates:
        return []
    res = []
    candidates.sort()
    def dfs(history, remain):
        if sum(history) == target:
            res.append(history)
            return
        if sum(history) > target:
            return
        if not remain:
            return
        for i in range(len(remain)):
            if i > 0 and remain[i] == remain[i-1]:
                continue
            if remain[i] <= target:
                dfs(history + [remain[i]], remain[i+1:])
    dfs([], candidates)
    return res