def isStrobogrammatic(self, num: str) -> bool:
    dic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    reverse = num[::-1]
    ls = []
    for i in range(len(reverse)):
        if reverse[i] not in dic:
            return False
        ls.append(dic[reverse[i]])
    return ''.join(ls) == num