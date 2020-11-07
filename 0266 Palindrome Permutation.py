def canPermutePalindrome(self, s: str) -> bool:
    if len(s) <= 1:
        return True
    dic = {}
    for i in s:
        dic[i] = dic.get(i,0) + 1
    
    count = 0
    for i in dic.values():
        if i % 2 != 0:
            count += 1
        if count >= 2:
            return False
    
    return True