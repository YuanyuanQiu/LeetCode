def maxLength(self, arr: List[str]) -> int:
    res = 0
    def dfs(history, remain):
        nonlocal res
        if not remain:
            return
        for i in range(len(remain)):
            if len(remain[i]) != len(set(remain[i])):
                continue
            if not set(history) & set(remain[i]):
                tmp = history + remain[i]
                res = max(res, len(tmp))
                dfs(tmp, remain[i+1:])
            # else:
            #     dfs(history, remain[i+1:])
    dfs('', arr)
    return res