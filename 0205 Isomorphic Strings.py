# 双字典
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    sdic = {}
    for i in range(len(s)):
        sdic[s[i]] = sdic.get(s[i],[]) + [i]
    
    tdic = {}
    for j in range(len(t)):
        tdic[t[j]] = tdic.get(t[j],[]) + [j]
    
    sv = list(sdic.values())
    tv = list(tdic.values())
    sv.sort()
    tv.sort()
    if sv == tv:
        return True
    else:
        return False


# 单字典 {s[i]:t[i]}
def isIsomorphic(s, t):
    dct = {}
    for i in range(len(s)):
        if s[i] not in dct:
            if t[i] in dct.values():
                return False
            dct[s[i]] = t[i]
        else:
            if dct[s[i]] != t[i]:
                return False
    return True


# 同构代表两个字符串中每个位置上字符在自身第一次出现的索引相同
def isIsomorphic(s, t):
    for i in range(len(s)):
        if s.index(s[i]) != t.index(t[i]):
            return False
    return True

print(isIsomorphic("abab","baba"))
        