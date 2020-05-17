'''
There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i],
or pipe in water from another well to it.

The costs to lay pipes between houses are given by the 7-array pipes,
where each pipes[i] = [house1, house2, cost] represents the cost to connect house1 and house2 together using a pipe.

Connections are bidirectional.

Find the minimum total cost to supply water to all houses.

Example 1:
Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation:
The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and
connect the other houses to it with cost 2 so the total cost is 3.

'''

#we model this problem as a graph problem
#Add a virtual node, connect it to houses with edges weighted by the costs to build wells in these houses.
#The problem is now reduced to a Minimum Spanning Tree problem.

#union find (Kruskal)
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