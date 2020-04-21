'''
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1-3-1-1-1 minimizes the sum.
'''

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

def minPathSum_NoExtraSpace(grid):
    if not grid: return 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0:
                grid[i][j] = grid[0][0]
            elif i == 0:
                grid[i][j] = grid[i][j - 1] + grid[i][j]
            elif j == 0:
                grid[i][j] = grid[i - 1][j] + grid[i][j]
            else:
                grid[i][j] = min(grid[i][j - 1], grid[i - 1][j]) + grid[i][j]

    return grid[-1][-1]

grid = [[]]
print(minPathSum(grid))