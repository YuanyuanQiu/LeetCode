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

def getRow(self, rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    dp = []
    for i in range(rowIndex+1):
        row = [None for _ in range(i+1)]
        row[0], row[-1] = 1, 1

        for j in range(1, len(row)-1):
            row[j] = dp[i-1][j-1] + dp[i-1][j]
        
        dp.append(row)
    
    return dp[-1]