 def myAtoi(s):
    s = s.strip()
    if not s:
        return 0
    flag = 1
    if s[0] == '-':
        flag = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]
    for i in range(len(s)):
        if not s[i].isnumeric():
            s = s[:i]
            break
    if not s:
        return 0
    s = flag * int(s)
    
    if s > 2**31 - 1:
        return 2**31 - 1
    elif s < -2**31:
        return -2**31
    else:
        return s


# lstrip() 方法用于截掉字符串左边的空格或指定字符
# ^：匹配字符串开头
# [\+\-]：代表一个+字符或-字符
# ?：前面一个字符可有可无
# \d：一个数字
# +：前面一个字符的一个或多个
# \D：一个非数字字符
# *：前面一个字符的0个或多个

def myAtoi(s):
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)

print(myAtoi(" "))















