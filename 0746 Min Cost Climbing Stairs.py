def minCostClimbingStairs(self, cost: List[int]) -> int:
    n = len(cost)
    # dp[i]表示到达i层以上需要的最小cost
    dp = [0] * n
    # 到达1层即dp[0]不需要cost
    # 到达2层即dp[1]需取0和1最小值
    dp[1] = min(cost[0], cost[1])
    for i in range(2,n):
        # 到达i+1即dp[i]有两种可能：i或i-1
        # 从i出发：dp[i-1] + cost[i]
        # 从i-1出发：dp[i-2] + cost[i-1]
        dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i-1])
    return dp[-1]