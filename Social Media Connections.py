def bestTrio(friends_nodes, friends_from, friends_to):
    dic = {}
    for i in range(len(friends_from)):
        dic[friends_from[i]] = dic.get(friends_from[i],[]) + [friends_to[i]]
        dic[friends_to[i]] = dic.get(friends_to[i],[]) + [friends_from[i]]
    # print(dic)
    ans = []
    for i in dic:
        for j in dic[i]:
            for k in dic[j]:
                if k in dic[i]:
                    ans.append(len(dic[i])+len(dic[j])+len(dic[k])-6)
    return min(ans)
    

print(bestTrio(6, [5,1,1,2,2,3,4], [6,2,3,3,4,4,5]))