# Dynamic Programming
#def longestPalindrome(s):
#    n = len(s)
#    dp = [[False] * n for _ in range(n)]
#    ans = ""
#    
#    # 枚举子串的长度 l+1
#    for l in range(n):
#        
#        # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
#        for i in range(n):
#            j = i + l
#            if j >= len(s):
#                break
#            
#            # 子串长度1：必为True
#            if l == 0:
#                dp[i][j] = True
#            # 子串长度2：相等为True
#            elif l == 1:
#                dp[i][j] = (s[i] == s[j])
#            # 子串长度>2
#            else:
#                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
#            
#            # l + 1 为子串长度
#            if dp[i][j] and l + 1 > len(ans):
#                ans = s[i:j+1]
#    return ans


# Expand Around Center
def expandAroundCenter(self, s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1

def longestPalindrome(self, s: str) -> str:
    start, end = 0, 0
    for i in range(len(s)):
        # 'a' -> 'bab'
        left1, right1 = self.expandAroundCenter(s, i, i)
        # 'aa' -> 'baab'
        left2, right2 = self.expandAroundCenter(s, i, i + 1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2
    return s[start: end + 1]


# Expand Around Center 2
def longestPalindrome(self, s: str) -> str:
    n = len(s)
    if n <= 1:
        return s
    # s[i:j+1]
    res = ''
    length = 0
    def expand(i,j):
        nonlocal length, res
        if i - 1 >= 0 and j + 1 < n and s[i-1] == s[j+1]:
            expand(i-1,j+1)
        else:
            if len(s[i:j+1]) > length:
                length = len(s[i:j+1])
                res = s[i:j+1]
    for i in range(n-1):
        expand(i,i)
        if s[i] == s[i+1]:
            expand(i,i+1)
    return res

print(longestPalindrome("babad"))