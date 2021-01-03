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
    if len(nums) <= 1:
        return [nums]
    
    res = []
    def backtrack(temp_list, remain):
        if not remain:
            res.append(temp_list)
            return
        
        for i in range(len(remain)):
            backtrack(temp_list + [remain[i]], remain[:i] + remain[i+1:])
     
    backtrack([], nums)
    return res


print(permute([1,2,3]))