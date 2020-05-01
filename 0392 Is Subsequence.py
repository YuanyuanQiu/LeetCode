def isSubsequence(s, t):
    cut = 0
    for i in s:
        if t.find(i,cut) ==-1:
            return False
        else:
            cut = t.find(i,cut)+1
    return True

print(isSubsequence('axc', 'ahbgdc'))