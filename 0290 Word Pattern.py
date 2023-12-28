def wordPattern(self, pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """
    ls = s.split()
    if len(ls)!= len(pattern):
        return False
    dic = dict() # {pattern:s}
    for i in range(len(pattern)):
        if pattern[i] in dic:
            if dic[pattern[i]] != ls[i]:
                return False
        elif ls[i] in dic.values():
            return False
        else:
            dic[pattern[i]] = ls[i]
    return True


def wordPattern(pattern, str):
    res=str.split()
    # pattern.index('a')返回pattern字符串中字符‘a’首次出现的位置
    return list(map(pattern.index, pattern))==list(map(res.index,res))

print(wordPattern('abba','dog cat cat fish'))