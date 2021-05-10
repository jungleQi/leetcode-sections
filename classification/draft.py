from collections import deque
def maxDistance(grid):
    N = len(grid)
    lands = [(i,j,0) for i in range(N) for j in range(N) if grid[i][j] == 1]
    if(len(lands) == N or len(lands) == 0): return -1

    dist = -1
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    q = deque(lands)
    while q:
        r,c,dist = q.popleft()
        for i,j in directions:
            if(r+i<0 or r+i>=N or j+c<0 or j+c>=N or grid[r+i][c+j] == 1): continue
            grid[r+i][c+j] = 1
            q.append((r+i,c+j, dist+1))
    return dist

grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
print(maxDistance(grid))