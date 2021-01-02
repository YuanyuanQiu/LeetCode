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
        candidates = sorted(candidates)

        ans = []

        def find(s, use, remain):
            for i in range(s, len(candidates)):
                c = candidates[i]
                if c == remain: # 满足条件，加入答案
                    ans.append(use + [c])
                if c < remain: # 不足，继续递归
                    find(i, use + [c], remain - c) # 往后缩小candidate
                if c > remain: # 超出，退出
                    return
        
        find(0, [], target)

        return ans


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)