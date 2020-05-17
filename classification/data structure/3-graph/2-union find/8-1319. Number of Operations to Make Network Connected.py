'''
There are n computers numbered from 0 to n-1 connected by ethernet cables connections
forming a network where connections[i] = [a, b] represents a connection between computers a and b.
Any computer can reach any other computer directly or indirectly through the network.

Given an initial computer network connections.
You can extract certain cables between two directly connected computers,
and place them between any pair of disconnected computers to make them directly connected.
Return the minimum number of times you need to do this in order to make all the computers connected.
If it's not possible, return -1.

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
'''

class UnionFind(object):
    def __init__(self, N):
        self.parent = range(N)
        self.conn = 1
        self.extra = 0

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        if ri == rj:
            self.extra += 1
        else:
            self.conn += 1
            self.parent[ri] = rj

def makeConnected(n, connections):
    uf = UnionFind(n)
    for conn in connections:
        uf.union(conn[0], conn[1])
    return n - uf.conn if uf.conn + uf.extra >= n else -1