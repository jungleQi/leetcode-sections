'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''

import collections
def orangesRotting(grid):
    minTime = 0
    freshCnt = 0
    R,C = len(grid), len(grid[0])

    q = collections.deque()
    for i in range(R):
        for j in range(C):
            if(grid[i][j] == 2):
                q.append((i,j,0))
            elif(grid[i][j] == 1):
                freshCnt += 1

    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        r,c,minTime = q.popleft()
        for i,j in directions:
            if(r+i>= R or r+i<0 or c+j>=C or c+j<0 or grid[r+i][c+j] != 1): continue
            q.append((r+i, c+j, minTime+1))
            grid[r + i][c + j] = 2
            freshCnt -= 1

    return minTime if freshCnt == 0 else -1

grid = [[0,2]]
print(orangesRotting(grid))