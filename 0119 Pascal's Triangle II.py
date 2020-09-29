def getRow(rowIndex: int):
    if rowIndex == 0:
        return [1]
    if rowIndex == 1:
        return [1,1]
    
    pre = [1,1]
    for i in range(2,rowIndex+1):
        ans = [1]
        for j in range(len(pre)-1):
            ans.append(pre[j]+pre[j+1])
        ans.append(1)
        pre = ans
    
    return ans

print(getRow(4))