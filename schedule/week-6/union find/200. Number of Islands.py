#coding=utf-8

'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11000
11000
00100
00011

Output: 3
'''

def numIslands(grid):
    M,N = len(grid), len(grid[0])
    def dfs(i,j):
        if i >= M or i<0  or j >=N or j<0 or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)

    ans = 0
    for m in range(M):
        for n in range(N):
            if grid[m][n] == "1":
                ans += 1
                dfs(m,n)
    return ans

class UF(object):
    def __init__(self, m, n, grid):
        self.parent = {}
        for i in range(m):
            for j in range(n):
                #初始化Parent的精确性，为最后的根节点统计做准备
                if grid[i][j] == "1":
                    self.parent[(i,j)] = (i,j)

    def find(self,i,j):
        while (i,j) != self.parent[(i,j)]:
            self.parent[(i,j)] = self.parent[self.parent[(i,j)]]
            (i,j) = self.parent[(i,j)]
        return (i,j)

    def union(self, i,j, m,n):
        (ir, jr) = self.find(i,j)
        (mr, nr) = self.find(m,n)
        self.parent[(ir,jr)] = (mr, nr)

import collections
def numIslands_unionFind(grid):
    M,N = len(grid), len(grid[0])
    uf = UF(M, N, grid)
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "0": continue

            if i-1 >= 0 and grid[i-1][j] == "1":
                uf.union(i,j, i-1,j)
            if j-1 >= 0 and grid[i][j-1] == "1":
                uf.union(i,j, i,j-1)
    #sum的应用
    return sum(1 for node in uf.parent if node == uf.parent[node])



grid = [["1","0","1","0","0"]]
print(numIslands_unionFind(grid))