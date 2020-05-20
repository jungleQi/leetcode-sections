#coding=utf-8

import collections,sys

#以building为起始点遍历，在以下两种情况下具有优势：
# 1.如果不存在符合的空地，就很快能判断出来，不需要对每个building进行多次循环
# 2.当buliding数量 < empty数量，bfs次数也会更少
# 3.以building为起始点，具有很强的凝聚性，能以某个building为中心扩张出去的网络，如果包括了所有的building，
#   那么网络之中的empty也是可以到达所有的building，并且这些empty才是最佳的候选者，网络之外的empty实际上远离了网络重心
def shortestDistance(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid or not grid[0]: return -1
    m, n, buildings = len(grid), len(grid[0]), sum(v for line in grid for v in line if v == 1)
    hit = [[[0, 0] for _ in range(n)] for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(start_x, start_y):
        buildVisitors, visitor = 1, [[False] * n for _ in range(m)]
        q = collections.deque([(start_x, start_y, 0)])
        visitor[start_x][start_y] = True

        while q:
            x, y, d = q.popleft()
            for dir in directions:
                row, col = x + dir[0], y + dir[1]
                if row < 0 or row >= m or col < 0 or col >= n or visitor[row][col]:
                    continue

                visitor[row][col] = True
                if grid[row][col] == 1:
                    buildVisitors += 1
                elif grid[row][col] == 0:
                    hit[row][col][0] += 1
                    hit[row][col][1] += d + 1
                    q.append((row, col, d + 1))
        return buildVisitors == buildings

    mindist = sys.maxint
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not bfs(i, j):
                return -1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0 and hit[i][j][0] == buildings:
                mindist = min(mindist, hit[i][j][1])

    return mindist if mindist != sys.maxint else -1