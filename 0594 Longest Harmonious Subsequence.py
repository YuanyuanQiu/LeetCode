def findLHS(nums):
    dic = {}
    for i in nums:
        dic[i] = dic.get(i,0)+1
    
    count = 0
    for i in dic:
        if i+1 in dic:
            count = max(count, dic[i]+dic[i+1])
    return count

print(findLHS([]))