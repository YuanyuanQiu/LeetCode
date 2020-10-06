def titleToNumber(s):
    origin = ord('A')
    s = s[::-1]
    ans = 0
    for i in range(len(s)):
        gap = ord(s[i]) - origin
        ans += pow(26,i)*(1 + gap)
    return ans

print(titleToNumber('AA'))
        