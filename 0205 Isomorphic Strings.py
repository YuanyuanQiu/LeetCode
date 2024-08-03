def isIsomorphic(self, s: str, t: str) -> bool:
    m, n = len(s), len(t)
    if m != n:
        return False
    # create mapping s[i]:t[i]
    dic = dict()
    for i in range(m):
        if s[i] in dic:
            if dic[s[i]] != t[i]:
                return False
        else:
            if t[i] in dic.values():
                return False
            else:
                dic[s[i]] = t[i]
    return True