def minPathSum(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid: return 0

    row = len(grid)
    col = len(grid[0])
    dp = [[float("inf")] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                dp[0][0] = grid[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + grid[i][j]
    return dp[-1][-1]