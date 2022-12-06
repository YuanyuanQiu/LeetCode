def isIsomorphic(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dic = {}
    for i in range(len(s)):
        if (t[i] in dic.values() or s[i] in dic) and dic.get(s[i], 'error') != t[i]:
            return False
        dic[s[i]] = t[i]
    return True