'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

def numIslands(grid):
    def _helper(grid, x, y, m, n):
        if x>=m or y>=n or x<0 or y<0 or grid[x][y] == "0":
            return
        grid[x][y] = "0"
        _helper(grid, x - 1, y, m, n)
        _helper(grid,x+1,y,m,n)
        _helper(grid, x, y-1, m, n)
        _helper(grid, x, y+1, m, n)

    m = len(grid)
    if not m: return 0
    n = len(grid[0])

    lands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                lands += 1
                _helper(grid, i,j, m,n)
    return lands

from collections import deque
def numIslands_bfs(grid):
    if not grid: return 0

    lands = set([(i, j) for j in xrange(len(grid[0])) for i in xrange(len(grid)) if grid[i][j] == '1'])
    landcnt = 0
    while lands:
        landcnt += 1
        x,y = lands.pop()
        connect = deque()
        connect.append((x,y))
        while connect:
            x, y = connect.popleft()
            if (x + 1, y) in lands:
                connect.append((x + 1, y))
                lands.remove((x + 1, y))
            if (x - 1, y) in lands:
                connect.append((x - 1, y))
                lands.remove((x - 1, y))
            if (x, y + 1) in lands:
                connect.append((x, y + 1))
                lands.remove((x, y + 1))
            if (x, y - 1) in lands:
                connect.append((x, y - 1))
                lands.remove((x, y - 1))
    return landcnt



#grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid = [["1","0","1","1","1"],
        ["1","0","1","0","1"],
        ["1","1","1","0","1"]]
print(numIslands_bfs(grid))

