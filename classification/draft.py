#coding=utf-8
from utils import Node
import heapq
import collections

class UF(object):
    def __init__(self, N):
        self.parent = range(N+1)

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        if ri != rj:
            self.parent[ri] = rj
            return True
        else:
            return False

def findRedundantConnection(edges):
    N = len(edges)
    uf = UF(N)

    for edge in edges:
        if not uf.union(edge[0], edge[1]):
            return edge

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print findRedundantConnection(edges)