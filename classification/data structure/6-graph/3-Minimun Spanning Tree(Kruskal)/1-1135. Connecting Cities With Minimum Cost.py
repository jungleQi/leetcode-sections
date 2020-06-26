#coding=utf-8

'''
There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.
(A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities,
there exists a path of connections (possibly of length 1) that connects those two cities together.
The cost is the sum of the connection costs used. If the task is impossible, return -1.
'''

import collections
def minimumCost(N, connections):
    def travel(cur, cost):
        if sum(visitor.values()) == N:
            #print visitor, cost
            ret.append(cost)
            return

        for neighbor, curCost in graph[cur]:
            if visitor[neighbor]: continue
            visitor[neighbor] = True
            cost += curCost
            travel(neighbor, cost)
            #visitor[neighbor] = False

    graph = collections.defaultdict(list)
    for conn in connections:
        graph[conn[0]].append([conn[1],conn[2]])
        graph[conn[1]].append([conn[0],conn[2]])

    visitor = {city:False for city in range(1,N+1)}
    ret = []
    visitor[1] = True
    travel(1, 0)

    return min(ret) if ret else -1

#关键
# 1.对connections的cost进行排序
# 2.将当前连接并入一个并查集
# 3.如果当前connect的两个city已经在一个集合中，那这个connect应该放弃，因为已有的连接方式优于这次连接
#
class UnionFind(object):
    def __init__(self, N):
        self.parent = {i:i for i in range(1,N+1)}

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

def minimumCost_unionFind(N, connections):
    connections.sort(key=lambda x:x[2])
    uf = UnionFind(N)
    ans = 0
    for conn in connections:
        if uf.union(conn[0], conn[1]):
            ans += conn[2]

    return ans if sum([1 for i in range(1,N+1) if i == uf.parent[i]]) == 1 else -1

N = 4
connections = [[1,2,3],[3,4,4]]

print(minimumCost_unionFind(N, connections))
