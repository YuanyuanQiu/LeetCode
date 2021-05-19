# dynamic programming
def coinChange(self, coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0
    if amount < min(coins):
        return -1
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0
    for c in coins:
        for i in range(c,amount+1):
            dp[i] = min(dp[i], dp[i-c] + 1)
    return -1 if dp[-1] == float('inf') else dp[-1]