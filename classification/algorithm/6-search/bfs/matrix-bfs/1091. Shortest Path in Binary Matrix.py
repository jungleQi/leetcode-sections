import collections

def shortestPathBinaryMatrix(grid):
    N = len(grid)
    if (N == 1 and grid[0][0] == 0):
        return 1

    q = collections.deque()
    if grid[0][0] == 0:
        q.append((0, 0, 1))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    while q:
        r, c, shortestPath = q.popleft()
        for i, j in directions:
            if (r + i >= N or r + i < 0 or c + j >= N or c + j < 0 or grid[r + i][c + j] != 0):
                continue
            if (r + i == N - 1 and c + j == N - 1 and grid[r + i][c + j] == 0):
                return shortestPath + 1
            q.append((r + i, c + j, shortestPath + 1))
            grid[r + i][c + j] = 1
    return -1

grid = [[1,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid))