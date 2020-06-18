class UnionFind(object):
    def __init__(self, M, N, grid):
        self.count = M * N
        self.parent = {}
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    idx = (i * N + j) if i >= 1 else j
                    self.parent[idx] = idx

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        if ri != rj:
            self.parent[rj] = ri

    def maxUnion(self):
        counter = collections.defaultdict(int)
        for i in self.parent.keys():
            ri = self.find(i)
            counter[ri] += 1

        ret = sorted(counter.values())
        if not ret:
            return 0
        else:
            return ret[-1]

def maxAreaOfIsland(grid):
    M, N = len(grid), len(grid[0])
    uf = UnionFind(M, N, grid)
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0: continue
            if i > 0 and grid[i - 1][j] == 1:
                uf.union((i - 1) * N + j, i * N + j)
            if j > 0 and grid[i][j - 1] == 1:
                uf.union(i * N + j - 1, i * N + j)

    return uf.maxUnion()