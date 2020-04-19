#coding=utf-8
from utils import Node
import heapq
import collections

class UF(object):
    def __init__(self, n):
        self.parent = range(n)

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self,i,j):
        ri,rj = self.find(i), self.find(j)
        if ri != rj:
            self.parent[ri] = rj

import collections
def countComponents(n, edges):
    uf = UF(n)
    for edge in edges:
        uf.union(edge[0],edge[1])

    return sum([1 for node in range(n) if node == uf.parent[node]])

nums = [[0, 1], [1, 2], [2, 3], [3, 4]]
n = 5
print countComponents(n, nums)