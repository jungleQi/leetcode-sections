#coding=utf-8
from utils import Node
import heapq
import collections

class unionFind(object):
    def __init__(self, n):
        self.parent = range(n+1)

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        if ri == rj:
            return False
        else:
            self.parent[ri] = rj
            return True

def minCostToSupplyWater(n, wells, pipes):
    p = [(c, f, t) for f, t, c in pipes]
    w = [(c, 0, i) for i, c in enumerate(wells, 1)]

    uf = unionFind(n)
    ans, edgeCnt = 0, 0
    for c, f, t in sorted(p+w):
        if edgeCnt >= n: break
        if uf.union(f, t):
            ans += c
    return ans

n = 3
wells = [1,2,2]
pipes = [[1,2,1],[2,3,1]]
print minCostToSupplyWater(n, wells, pipes)