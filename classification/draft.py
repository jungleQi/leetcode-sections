#coding=utf-8
from utils import Node
import heapq
import collections


def calcEquation(equations, values, queries):
    parent = dict()

    def find(x):
        px, pv = parent.setdefault(x, (x, 1.0))
        if px != x:
            rx,rv = find(px)
            parent[x] = rx, rv*pv
        return parent[x]

    def union(i,j, load):
        (ri, vi), (rj, vj) = find(i), find(j)
        if not load:
            return vi/vj if ri == rj else -1.0
        else:
            parent[ri] = rj, load*vj/vi

    for (i,j), v in zip(equations, values):
        union(i,j,v)

    return [union(i,j,0) if i in parent and j in parent else -1.0 for i, j in queries]

equations = [["a","b"],["e","f"],["b","e"]]
values = [3.4,1.4,2.3]
queries = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]
print calcEquation(equations, values, queries)