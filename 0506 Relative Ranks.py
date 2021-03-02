#def findRelativeRanks(self, score: List[int]) -> List[str]:
#    N = len(score)
#    if N == 0:
#        return score
#    
#    sort = sorted(score, reverse = True)
#    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
#    for i in range(N):
#        rank = sort.index(score[i])
#        if rank <3:
#            score[i] = medals[rank]
#        else:
#            score[i] = str(rank+1)
#    
#    return score


def findRelativeRanks(self, score: List[int]) -> List[str]:
    s = sorted(score, reverse=True)
    dic = {}
    for i in range(len(s)):
        dic[s[i]] = i + 1
    res = []
    medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    for j in score:
        if dic[j] <= 3:
            res.append(medals[dic[j]-1])
        else:
            res.append(str(dic[j]))
    return res



print(findRelativeRanks([10,3,8,9,4]))
        
    
    
    
    
    