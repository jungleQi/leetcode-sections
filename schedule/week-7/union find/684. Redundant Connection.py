'''
In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N),
with one additional edge added. The added edge has two different vertices chosen from 1 to N,
and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v,
that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes.
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


class DSU(object):
    def __init__(self):
        self.par = range(1001)
        self.rnk = [0]*1001

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr,yr = self.find(x), self.find(y)
        if xr == yr:
            return False
        if self.rnk[xr] > self.rnk[yr]:
            self.par[yr] = xr
        elif self.rnk[xr] < self.rnk[yr]:
            self.par[xr] = yr
        else:
            self.par[xr] = yr
            self.rnk[xr] += 1
        return True



def findRedundantConnection_I(edges):
    dsu = DSU()
    for edge in edges:
        if not dsu.union(*edge):
            return edge

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(findRedundantConnection_I(edges))