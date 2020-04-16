#coding=utf-8
from utils import Node
import heapq
import collections

class UF(object):
    def __init__(self, M, N, grid):
        self.parent = {}
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    self.parent[(i,j)] = (i,j)

    def find(self, i, j):
        if (i,j) != self.parent[(i,j)]:
            self.parent[(i,j)] = self.find(self.parent[(i,j)])
        return self.parent[(i,j)]

    def union(self,i,j, m,n):
        (ri, rj) = self.find(i,j)
        (rm, rn) = self.find(m, n)
        self.parent[(ri,rj)] = (rm, rn)

def numIslands_unionFind(grid):
    if not grid : return 0
    M,N = len(grid), len(grid[0])
    uf = UF(M, N, grid)
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '0': continue
            if i-1 >= 0:
                uf.union(i,j,i-1,j)
            if j-1 >= 0:
                uf.union(i,j,i,j-1)

    return sum([1 for node in uf.parent if node == uf.parent[node]])

