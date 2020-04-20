import sys
def minPathSum(grid):
    M,N = len(grid), len(grid[0])
    dp = [[sys.maxint for _ in range(N+1)] for _ in range(M+1)]

    for i in range(1,M+1):
        for j in range(1,N+1):
            if i == 1 and j == 1:
                dp[i][j] = grid[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1],dp[i-1][j])+grid[i-1][j-1]

    return dp[-1][-1]

grid = [[]]
print(minPathSum(grid))