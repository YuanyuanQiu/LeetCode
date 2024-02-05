class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        cur_sum = 0
        min_sum = float('inf')
        
        for i in range(n):
            cur_sum += gas[i] - cost[i]
            min_sum = min(min_sum, cur_sum)
        
        # 如果gas的总和小于cost总和，那么无论从哪里出发，一定是跑不了一圈的
        if cur_sum < 0:
            return -1
        # 如果累加没有出现负数,0就是起点
        if min_sum >= 0:
            return 0
        # 如果累加的最小值是负数，汽车就要从非0节点出发从后向前
        # 看哪个节点能把这个负数填平，能把这个负数填平的节点就是出发节点。
        for j in range(n - 1, 0, -1):
            min_sum += gas[j] - cost[j]
            if min_sum >= 0:
                return j
        
        return -1