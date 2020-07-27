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
        size = len(candidates)
        if size == 0:
            return []

        # 剪枝是为了提速，在本题非必需
        candidates.sort()
        # 在遍历的过程中记录路径，它是一个栈
        path = []
        res = []
        # 注意要传入 size ，在 range 中， size 取不到
        self.__dfs(candidates, 0, size, path, res, target)
        return res

    def __dfs(self, candidates, begin, size, path, res, target):
        # 先写递归终止的情况
        if target == 0:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 path.copy()
            res.append(path[:])
            return

        for index in range(begin, size):
            residue = target - candidates[index]
            # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
            if residue < 0:
                break
            path.append(candidates[index])
            # 因为下一层不能比上一层还小，起始索引还从 index 开始
            self.__dfs(candidates, index, size, path, res, residue)
            path.pop()


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    print(result)