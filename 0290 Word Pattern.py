def wordPattern(self, pattern: str, s: str) -> bool:
    ls = s.split(' ')
    m, n = len(pattern), len(ls)
    if m != n:
        return False
    # create mapping pattern[i]:ls[i]
    dic = {}
    for i in range(m):
        if pattern[i] in dic:
            if dic[pattern[i]] != ls[i]:
                return False
        else:
            if ls[i] in dic.values():
                return False
            dic[pattern[i]] = ls[i]
    return True