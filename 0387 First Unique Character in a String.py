# def firstUniqChar(s):
#     dic = {}
#     repeat = []
#     for i in s:
#         if i not in repeat:
#             if i not in dic:
#                 dic[i]=1
#             else:
#                 dic.pop(i)
#                 repeat.append(i)
#     if dic == {}:
#         return -1
#     else:
#         return s.index(list(dic.keys())[0])

def firstUniqChar(s):
    dicts={}
    for i in s:
        dicts[i]=dicts.get(i,0)+1
    for i in range(len(s)):
        if dicts[s[i]]==1:
            return i
    return -1

print(firstUniqChar("loveleetcode"))
        