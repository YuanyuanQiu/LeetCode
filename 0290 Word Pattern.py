# def wordPattern(pattern, str):
#     ls = str.split()
#     dic = {}
#     if len(ls) != len(pattern):
#         return False
#     for i in range(len(pattern)):
#         if pattern[i] not in dic:
#             dic[pattern[i]] = ls[i]
#         else:
#             if dic[pattern[i]] != ls[i]:
#                 return False
#         if list(dic.keys())[list(dic.values()).index(ls[i])]!= \
#             pattern[i]:
#             return False
#     return True


def wordPattern(pattern, str):
    res=str.split()
    # pattern.index('a')返回pattern字符串中字符‘a’首次出现的位置
    return list(map(pattern.index, pattern))==list(map(res.index,res))

print(wordPattern('abba','dog cat cat fish'))