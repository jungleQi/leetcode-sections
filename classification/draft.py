#coding=utf-8

from utils import *
import collections

def validTree(n, edges):
    adjacent = [[] for _ in range(n)]
    for edge in edges:
        adjacent[edge[0]].append(edge[1])
        adjacent[edge[1]].append(edge[0])

    def dfs(prev, cur):
        for nei in adjacent[cur]:
            #坑：如果不放在 if nei in visitor 之前 进行判断，会出现误判
            if nei == prev: continue
            if nei in visitor: return False

            visitor.add(nei)
            ret = dfs(cur, nei)
            if not ret: return False

        return True

    #定义在外部，嵌套函数也可以操作访问
    visitor = set([0])
    return dfs(-1, 0) and len(visitor) == n

n = 4
edges = [[0,1],[2,3],[1,2]]
print(validTree(n, edges))




