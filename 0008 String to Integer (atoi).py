def myAtoi(self, s: str) -> int:
    # 去除空字符
    s = s.strip()
    if not s:
        return 0
    
    # 判断正负
    flag = 1
    if s[0] == '-':
        flag = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    
    # 截取数字
    for i in range(len(s)):
        if not s[i].isnumeric():
            s = s[:i]
            break
    if not s: # 无数字
        return 0
    s = flag * int(s)
    
    # 区间
    if s > 2**31 - 1:
        return 2**31 - 1
    elif s < -2**31:
        return -2**31
    else:
        return s