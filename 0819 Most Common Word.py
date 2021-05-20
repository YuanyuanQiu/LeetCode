def mostCommonWord(paragraph, banned):
    paragraph = paragraph.lower()
    for c in "!?',;.":
        paragraph = paragraph.replace(c, " ")
    ls = paragraph.split()
    dic = {}
    for i in ls:
        if i not in banned:
            dic[i] = dic.get(i,0) + 1
    return sorted(list(dic.keys()), key=lambda x: dic[x])[-1]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))