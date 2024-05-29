#  滑动窗口
def lengthOfLongestSubstring(s):
    n = len(s)
    if n <= 1:
        return n
    window = set()
    res = 0
    r = 0
    for i in range(n):
        if i > 0:
            window.remove(s[i-1])
        while r < n and s[r] not in window:
            window.add(s[r])
            r += 1
        res = max(res, r - i)
    return res

def lengthOfLongestSubstring(self, s: str) -> int:
    n = len(s)
    if n <= 1:
        return n
    l, r = 0, 1
    ans = 0
    sub = set(s[0])
    while r < n:
        if s[r] in sub:
            sub.remove(s[l])
            l += 1
        else:
            sub.add(s[r])
            r += 1
            ans = max(ans, r-l)
    return ans