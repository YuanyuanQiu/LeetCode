def isAnagram(s,t):
    if set(s) != set(t) or len(s) != len(t):
        return False
    
    for i in s:
        if i in t:
            t = t.replace(i,'',1)
        else:
            return False
        
    return True


def isAnagram(self, s: str, t: str) -> bool:
    return collections.Counter(s) == collections.Counter(t) 


print(isAnagram('rat', 'car'))