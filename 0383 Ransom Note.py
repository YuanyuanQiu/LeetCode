def canConstruct(ransomNote, magazine):
    from collections import Counter
    dic = Counter(magazine)
    for i in ransomNote:
        if i not in magazine or dic[i]==0:
            return False           
        else:
            dic[i]-=1         
    return True

print(canConstruct("fffbfg", "effjfggbffjdgbjjhhdegh"))