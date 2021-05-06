# 暴力（超时）
def numDecodings(self, s: str) -> int:
    ls = set(str(i) for i in range(1,27))
    res = 0
    def dfs(s):
        nonlocal res
        if not s:
            res += 1
            return
        if s[0] in ls:
            dfs(s[1:])
        if len(s) > 1 and s[:2] in ls:
            dfs(s[2:])
        return
    dfs(s)
    return res

# 动态规划
def numDecodings(self, s: str) -> int:
    if not s or s[0] == '0':
        return 0
    n = len(s)
    # dp[i]: decode ways s[:i] (till s[i-1])
    dp = [0 for _ in range(n+1)]
    dp[0] = 1 # 空字符串可以有1种解码方法，解码出一个空字符串
    for i in range(1,n+1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        if i > 1 and s[i-2] != '0' and int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    return dp[n]