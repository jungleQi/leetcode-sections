'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
write a function to find the number of connected components in an undirected 6-graph.

Example 1:
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4

Output: 2
'''

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

def countComponents(n, edges):
    uf = UF(n)
    for edge in edges:
        uf.union(edge[0],edge[1])

    return sum([1 for node in range(n) if node == uf.parent[node]])

n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
print countComponents(n, edges)
