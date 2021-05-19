def numSquares(self, n: int) -> int:
    if n <= 2:
        return n
    dp = [float('inf') for _ in range(n+1)]
    dp[0] = 0
    square_nums = [i**2 for i in range(0,int(sqrt(n))+1)]
    for i in range(1,n+1):
        for square in square_nums:
            dp[i] = min(dp[i], dp[i-square] + 1)
    return dp[-1]