#  滑动窗口
#def lengthOfLongestSubstring(self, s: str) -> int:
#    n = len(s)
#    if n < 2:
#        return n
#    window = s[0]
#    l = 1
#    res = 0
#    while l < n:
#        # s[l] not in window
#        while l < n and s[l] not in window:
#            window += s[l]
#            l += 1
#        # s[l] in window
#        res = max(len(window), res)
#        if l == n:
#            return res
#        idx = window.index(s[l])
#        window = window[idx+1:]
#        window += s[l]
#        l += 1
#    return res

def lengthOfLongestSubstring(s):
    ans = 0
    mark = set()  # 用集合标明是否有出现重复字母
    r = 0  # 右指针
    
    for i in range(len(s)): #左指针
        if i != 0:
            mark.remove(s[i - 1]) # 起点为i
        
        # 如果不满足条件说明r走到了s的尽头或r指向的元素重复    
        while r < len(s) and s[r] not in mark:
            mark.add(s[r])  # 将当前r指向的字母加入集合
            r += 1 # 右指针右移
        
        ans = max(ans, r - i)  # 在每一个位置更新最大值

    return ans


print(lengthOfLongestSubstring("pwwkew"))