class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 必须保留这个判断，否则切片后的长度可能导致 helper 内部越界
        if n <= 2: 
            return max(nums)

        def helper(houses):
            # 1. 获取当前切片的实际长度，不要用外面的 n
            m = len(houses) 
            
            # 这里的边界判断其实因为外层 n>2 可以省略，但为了 helper 的独立性最好加上
            if m == 0: return 0
            if m == 1: return houses[0]
            
            pre2 = houses[0]
            pre1 = max(houses[0], houses[1])
            
            # 2. 使用 m (切片长度)
            for i in range(2, m): 
                cur = max(pre2 + houses[i], pre1)
                pre2 = pre1
                pre1 = cur
            
            # 3. 返回 pre1 而不是 cur，处理循环不执行的情况
            return pre1 

        # 情况1: 不抢第一间 (抢 nums[1] 到 nums[n-1])
        res1 = helper(nums[1:])
        
        # 情况2: 不抢最后一间 (抢 nums[0] 到 nums[n-2])
        res2 = helper(nums[:-1])

        return max(res1, res2)