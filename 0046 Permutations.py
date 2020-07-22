# # input single list, find next possible lists
# def next(ls,nums):
#     res = []
#     for i in list(set(nums) - set(ls)):
#         res.append(ls+[i])
#     return res

# def permute(nums):
#     temp = []
#     # first element
#     for i in nums:
#         temp.append([i])
    
    
#     while len(temp[0]) < len(nums):
#         res = []
#         for i in temp:
#             res += next(i,nums)
#         temp = res
    
#     return res

def permute(nums):
    res = []
    
    # 将num中数字逐步移至tmp，移完时返回结果
    def backtrack(nums, tmp):
        # 当nums为空时，返回结果
        if not nums:
            res.append(tmp)
            return 
        
        # 遍历后调用自身
        for i in range(len(nums)):
            # print(i,nums,nums[:i] + nums[i+1:],tmp + [nums[i]])
            backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
    
    backtrack(nums, [])
    
    return res

print(permute([1,2,3]))