def isAnagram(s,t):
    if len(s) != len(t):
        return False
    if set(s) != set(t):
        return False
    
    dict_s={}
    for i in s:
        if i not in dict_s:
            dict_s[i]=1
        else:
            dict_s[i]+=1
    
    dict_t={}
    for j in t:
        if j not in dict_t:
            dict_t[j]=1
        else:
            dict_t[j]+=1
        if dict_t[j]>dict_s[j]:
            return False
    
    if dict_s != dict_t:
        return False
    else:
        return True

print(isAnagram('rat', 'car'))