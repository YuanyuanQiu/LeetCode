def permuteUnique(nums):
    if not nums:
        return []
    res = []
    nums.sort()
    def dfs(history, remain):
        if not remain:
            res.append(history)
        for i in range(len(remain)):
            if i > 0 and remain[i] == remain[i-1]:
                continue
            dfs(history + [remain[i]], remain[:i] + remain[i+1:])
    dfs([], nums)
    return res