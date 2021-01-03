# # 动态规划
# def combinationSum(candidates, target):
#     dict = {}
#     for i in range(1,target+1):
#         dict[i]=[]
    
#     for i in range(1,target+1):
#         for j in candidates:
#             if i==j:
#                 dict[i].append([i])
#             elif i>j:
#                 for k in dict[i-j]:
#                     x = k[:]
#                     x.append(j)
#                     x.sort() # 升序，便于后续去重
#                     if x not in dict[i]:
#                         dict[i].append(x)

#     return dict[target]

# print(combinationSum(candidates = [2,3,6,7], target = 7))

# 回溯递归剪枝
class Solution:
    def combinationSum(candidates, target):
        if not candidates: #先解决空输入的情况
            return []
        
        candidates.sort()  #排序
        res=[]
        def backtrack(i,temp_sum,temp_list): 
            """
            i：遍历到candidates数组中第几个元素
            temp_sum：目前遍历数组的和
            temp_list：目前遍历的数组
            """
            if temp_sum==target:
                res.append(temp_list)
                return
            if temp_sum>target:
                return
            for j in range(i,len(candidates)):
                backtrack(j,temp_sum+candidates[j],temp_list+[candidates[j]])
        backtrack(0,0,[])
        return res

if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)