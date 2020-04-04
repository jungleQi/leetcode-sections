#coding=utf-8

'''
In this problem, a tree is an undirected direct graph that is connected and has no cycles.

The given input is a direct graph that started as a tree with N nodes (with distinct values 1, 2, ..., N),
with one additional edge added. The added edge has two different vertices chosen from 1 to N,
and was not an edge that already existed.

The resulting direct graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v,
that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting direct graph is a tree of N nodes.
If there are multiple answers, return the answer that occurs last in the given 2D-array.
The answer edge [u, v] should be in the same format, with u < v.
'''

import collections
def findRedundantConnection(edges):
    graph = collections.defaultdict(list)

    def dfs(u, v, pre, graph):
        if u == v: return True
        for w in graph[u]:
            if w == pre: continue
            ret = dfs(w, v, u, graph)
            if ret: return True
        return False

    ans = []
    for edge in edges:
        if dfs(edge[0],edge[1],0,graph):
            ans = edge
        else:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

    return ans


class UF(object):
    def __init__(self):
        self.par = dict()

    def find(self, x):
        #很巧妙的将par的初始化和par[x]的获取结合在一起
        #如果没有就初始化为指向自己，如果有父节点就返回父节点
        px = self.par.setdefault(x, x)
        if x != px:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self,x,y):
        px,py = self.find(x), self.find(y)
        if px == py:
            return False
        else:
            self.par[py] = px
            return True

def findRedundantConnection_I(edges):
    uf = UF()
    for edge in edges:
        if not uf.union(edge[0], edge[1]):
            return edge

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(findRedundantConnection_I(edges))