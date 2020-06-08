def matrixReshape(nums, r, c):
    if r*c != len(nums)*len(nums[0]):
        return nums
    
    ls = []
    for i in nums:
        for j in i:
            ls.append(j)

    ls1 = []
    for k in range(r):
        ls1.append(ls[k*c:k*c+c])
        
    return ls1

print(matrixReshape([[1,2,3,4]],2,2))