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

print(matrixReshape([[1,2,3,4]],2,2))