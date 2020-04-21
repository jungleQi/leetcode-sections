#coding=utf-8
from utils import Node
import heapq
import collections

def minPathSum(grid):
    if not grid: return 0

    M,N = len(grid), len(grid[0])
    dp = [[0]*N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            if i ==0 and j ==0 :
                dp[i][j] = grid[0][0]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]

    return dp[-1][-1]

grid = [[1]]
print minPathSum(grid)