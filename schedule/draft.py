class UF(object):
    def __init__(self, M, N):
        self.parent = {(i,j):(i,j) for i in range(M) for j in range(N)}

    def find(self, (i,j)):
        if (i,j) != self.parent[(i,j)]:
            self.parent[(i,j)] = self.find(self.parent[(i,j)])
        return self.parent[(i,j)]

    def union(self, i,j, m,n):
        (ri, rj) = self.find((i, j))
        (rm, rn) = self.find((m, n))
        self.parent[(ri, rj)] = (rm, rn)

import collections
def numIslands(grid):
    M,N = len(grid), len(grid[0])
    uf = UF(M, N)
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "0": continue
            if i-1>=0 and grid[i-1][j] == "1":
                uf.union(i,j,i-1,j)
            if j-1>=0 and grid[i][j-1] == "1":
                uf.union(i,j,i,j-1)

    count = set()
    for i in range(M):
        for j in range(N):
            if grid[i][j] == "0": continue
            count.add(uf.find((i,j)))

    return len(count)

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(numIslands(grid))