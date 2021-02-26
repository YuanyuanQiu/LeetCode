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


def firstUniqChar(self, s: str) -> int:
    sset = set(s)
    dic = {}
    for i in range(len(s)):
        if s[i] not in sset:
            continue
        elif s[i] in dic:
            sset.remove(s[i])
        else:
            dic[s[i]] = i
    if not sset:
        return -1
    ls = list(sset)
    ls.sort(key = lambda x: dic[x])
    return dic[ls[0]]


print(firstUniqChar("loveleetcode"))
        