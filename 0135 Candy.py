class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        # total candies
        ret = 1
        # 递增序列长度, 递减序列长度, previous candy
        inc, dec, pre = 1, 0, 1
        for i in range(1, n):
            if ratings[i] >= ratings[i-1]:
                dec = 0 # 递减序列归0
                # 当前同学和上一个同学分数相等时，直接分配1个就行，这样满足最小
                pre = (1 if ratings[i] == ratings[i - 1] else pre + 1)
                ret += pre
                inc = pre # 更新递增序列（即pre最新数量）
            else:
                dec += 1 # 递减序列+1
                # 当当前的递减序列长度和上一个递增序列等长时
                # 需要把最近的递增序列的最后一个同学也并进递减序列中。
                if dec == inc:
                    dec += 1
                # 把递减序列翻转后加的每个同学的糖果数量
                ret += dec
                # 递减数列的最后一个值一定分配为1
                pre = 1
        return ret
    
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left, right = [1] * n, [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        count = left[-1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            count += max(left[i], right[i])
        return count