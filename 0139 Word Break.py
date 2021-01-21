def wordBreak(s, wordDict):
    n = len(s)
    
    # s前i位是否可以由wordDict中的单词表示
    dp = [False for _ in range(n+1)]
    
    dp[0] = True
    
    # s[i:j]
    for i in range(n):
        for j in range(i+1, n+1):
            if dp[i] and s[i:j] in wordDict:
                dp[j] = True
    return dp[-1]