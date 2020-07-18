# DP
def combinationSum(candidates, target):
    dict = {}
    for i in range(1,target+1):
        dict[i]=[]
    
    for i in range(1,target+1):
        for j in candidates:
            if i==j:
                dict[i].append([i])
            elif i>j:
                for k in dict[i-j]:
                    x = k[:]
                    x.append(j)
                    x.sort() # 升序，便于后续去重
                    if x not in dict[i]:
                        dict[i].append(x)

    return dict[target]

print(combinationSum(candidates = [2,3,6,7], target = 7))