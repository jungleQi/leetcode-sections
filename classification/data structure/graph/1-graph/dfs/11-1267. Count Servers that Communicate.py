#coding=utf-8

'''
You are given a map of a server center, represented as a m * n integer matrix grid,
where 1 means that on that cell there is a server and 0 means that it is no server.
Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.
'''

def countServers_normal(grid):
    M,N = len(grid), len(grid[0])
    visitor = [[False]*N for _ in range(M)]

    count = 0
    for row in range(M):
        if sum(grid[row]) <= 1: continue
        for col in range(N):
            if grid[row][col] == 1:
                count += 1
                visitor[row][col] = True

    for col in range(N):
        colNums = [rows[col] for rows in grid]
        if sum(colNums) <= 1: continue
        for row in range(M):
            if grid[row][col] == 1 and not visitor[row][col]:
                count += 1

    return count

def countServers_nice(grid):
    total = 0
    for row in range(len(grid)):
        row_servers_num = sum(grid[row])
        if row_servers_num > 1:
            total += row_servers_num
        elif row_servers_num == 1:
            for r in range(len(grid)):
                if grid[r][grid[row].index(1)] == 1 and r != row:
                    total += 1
                    break
    return total

#用DFS来解决，显得比较拧巴：
# 1.因为如果画出递归树(有向图)，这个递归树会非常多的边，每条边都需要去判断

import collections
def countServers_dfs(grid):
    def dfs(row, col):
        if row<0 or row>=M or col<0 or col>=N or visitor[row][col] or not grid[row][col]:
            return 0

        p = q = 0
        visitor[row][col] = True
        for item in rows[row]:
            p += dfs(item[0], item[1])
        for item in cols[col]:
            q += dfs(item[0], item[1])

        return p+q+1

    M, N = len(grid), len(grid[0])
    visitor = [[False]*N for _ in range(M)]
    rows = collections.defaultdict(list)
    cols = collections.defaultdict(list)

    ans = 0
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                rows[i].append([i,j])
                cols[j].append([i,j])

    for i in range(M):
        for j in range(N):
            if not visitor[i][j] and grid[i][j]:
                ret = dfs(i,j)
                ans += (ret if ret > 1 else 0)
    return ans

grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
print countServers_dfs(grid)