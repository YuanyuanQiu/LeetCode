def findJudge(N, trust):
    if trust == []:
        if N == 1:
            return N
        else:
            return -1
    
    no_judge = set()
    judge = {}
    
    for i in trust:
        if i[0] in judge:
            del judge[i[0]]
        no_judge.add(i[0])

        if i[1] not in no_judge:
            judge[i[1]] = judge.get(i[1],0) + 1

    if len(judge) == 1 and list(judge.values())[0] == N-1:
        return list(judge.keys())[0]
    else:
        return -1

print(findJudge(3, [[1,3],[2,3]]))