def maxLength(self, arr: List[str]) -> int:
    res = 0
    def backtrack(history, remain):
        nonlocal res
        if not remain:
            res = max(res, len(history))
        for i in range(len(remain)):
            if len(remain[i]) != len(set(remain[i])):
                continue
            if not(set(history) & set(remain[i])):
                res = max(res,len(history+remain[i]))
                backtrack(history+remain[i], remain[i+1:])
            else:
                backtrack(history, remain[i+1:])
    backtrack('', arr)
    return res