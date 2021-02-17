def matrixReshape(nums, r, c):
    if r*c != len(nums)*len(nums[0]):
        return nums
    
    ls = []
    for i in nums:
        for j in i:
            ls.append(j)

    res = []
    for k in range(r):
        res.append(ls[k*c:k*c+c])
        
    return res


def matrixReshape(nums, r, c):
    m, n = len(nums), len(nums[0])
    if m * n != r * c:
        return nums
    
    ans = [[0] * c for _ in range(r)]
    for x in range(m * n):
        ans[x // c][x % c] = nums[x // n][x % n]
    
    return ans


print(matrixReshape([[1,2,3,4]],2,2))