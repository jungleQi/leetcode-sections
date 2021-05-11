'''
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land,
find a water cell such that its distance to the nearest land cell is maximized, and return the distance.
If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
'''
import collections

#water入列，单独入队出队比较正确；初始队列，所有的water一起进去，然后BFS，会比较混乱
def maxDistance(grid):
    N = len(grid)
    waters = [(i,j,0) for i in range(N) for j in range(N) if grid[i][j] == 0]

    maxDist = -1
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for water in waters:
        q = collections.deque([water])
        visitor = set([(water[0],water[1])])

        while q:
            r,c,d = q.popleft()

            attachLand = False
            for i,j in directions:
                if(0<=r+i<N and 0<=c+j<N and (r+i, c+j) not in visitor):
                    if(grid[r+i][c+j] == 1):
                        attachLand = True
                        break
                    else:
                        q.append((r+i, c+j, d+1))
                        visitor.add((r+i, c+j))
            if attachLand:
                maxDist = max(maxDist, d+1)
                break

    return maxDist

#从land入列，开始扩展，就契合题目要求的每个的最近距离集合中，最大的数
def maxDistance(grid):
    N = len(grid)
    lands = [(i, j, 0) for i in range(N) for j in range(N) if grid[i][j] == 1]
    if (len(lands) == N * N or len(lands) == 0): return -1

    dist = -1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = collections.deque(lands)
    while q:
        r, c, dist = q.popleft()
        for i, j in directions:
            if (r + i < 0 or r + i >= N or j + c < 0 or j + c >= N or grid[r + i][c + j] == 1): continue
            grid[r + i][c + j] = 1
            q.append((r + i, c + j, dist + 1))
    return dist

grid = [[1,0,0],[0,0,0],[0,0,0]]
print(maxDistance(grid))