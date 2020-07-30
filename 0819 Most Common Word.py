def mostCommonWord(paragraph, banned):
    banned = set(banned)
    
    for c in "!?',;.":
        paragraph = paragraph.replace(c, " ")
        
    ls = paragraph.lower().split()
    
    dic = {}
    for i in ls:
        if i not in banned:
            dic[i] = dic.get(i,0) + 1
    
    ans = ''
    best = 0
    for j in dic:
        if dic[j] > best:
            ans = j
            best = dic[j]
        
    return ans

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))