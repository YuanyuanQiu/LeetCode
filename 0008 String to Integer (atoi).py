# def myAtoi(s):
#     s = s.strip(' ')
    
#     if s == '' or s == '-' or s == '+':
#         return 0
    
#     if s[0].isdigit() == False and s[0] not in '-+':
#         return 0
    
#     if s[0] in '-+':
#         if s[1].isdigit():
#             new = s[0]
#             s = s[1:]
#         else:
#             return 0
#     else:
#         new = ''

#     for i in s:
#         if i.isdigit():
#             new += i
#         else:
#             break
    
#     res = int(new)
#     return max(min(res, 2**31 - 1), 2**31 * -1)


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















