# def repeatedSubstringPattern(s: str) -> bool:
#     length = len(s)
#     if length < 2:
#         return False
#     n = 1
#     while n < length:
#         if length % n != 0:
#             pass
#         times = int(length / n)
#         if s[:n] * times == s:
#             return True
#         n += 1
#     return False


def repeatedSubstringPattern(self, s: str) -> bool:
    if not s:
        return True
    n = len(s)
    for i in range(n//2):
        if s == s[:i+1] * (n//(i + 1)):
            return True
    return False

'''
构建双倍链：如果s中包含重复的子字符串，那么说明s中至少包含两个子字符串，
s+s至少包含4个字串，前后各去掉一位，查找s是否在新构建的字符串中。
'''
def repeatedSubstringPattern(s: str) -> bool:
    return s in (s+s)[1:-1]

print(repeatedSubstringPattern('abcabcabcabc'))