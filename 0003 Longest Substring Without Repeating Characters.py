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


print(lengthOfLongestSubstring("pwwkew"))