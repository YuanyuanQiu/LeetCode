# 对于一个子串而言，如果它是回文串，并且长度大于 22，那么将它首尾的两个字母去除之后，
# 它仍然是个回文串。
def longestPalindrome(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)] # flag
    ans = ""
    # 枚举子串的长度 l+1
    for l in range(n):
        # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
        for i in range(n):
            j = i + l
            if j >= len(s):
                break
            
            if l == 0: # 1个字符
                dp[i][j] = True
            elif l == 1: # 2个字符
                dp[i][j] = (s[i] == s[j])
            else: # 3个及以上字符
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                
            if dp[i][j] and l + 1 > len(ans):
                ans = s[i:j+1]
    return ans

print(longestPalindrome("babad"))