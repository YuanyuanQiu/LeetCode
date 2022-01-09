def balancedStringSplit(self, s: str) -> int:
    n = len(s)
    if n == 1:
        return 0
    l = 0
    r = 1
    res = 0
    while r <= n - 1:
        ls = s[l:r+1].count('L')
        rs = s[l:r+1].count('R')
        if ls == rs:
            res += 1
            l = r + 1
        r += 1
    return res