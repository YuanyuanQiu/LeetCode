def minDistance(self, word1: str, word2: str) -> int:
    n1 = len(word1)
    n2 = len(word2)
    if n1 * n2 == 0:
        return n1 + n2
    
    # dp[i][j]: distance from word1[:i] to word2[:j]
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    
    # 边界初始化
    for i in range(n1 + 1):
        dp[i][0] = i
    for j in range(n2 + 1):
        dp[0][j] = j
    
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            add1 = dp[i-1][j] + 1 # word1增加一个字符
            add2 = dp[i][j-1] + 1 # word2增加一个字符
            change = dp[i-1][j-1]
            if word1[i-1] != word2[j-1]: # 改变一个字符
                change += 1
            dp[i][j] = min(add1, add2, change)
    
    return dp[n1][n2]