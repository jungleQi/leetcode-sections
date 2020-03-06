
class UF(object):
    def __init__(self, N):
        self.N = N
        self.parent = range(self.N)

    def find(self, i):
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        ri,rj = self.find(i), self.find(j)
        if ri != rj:
            self.parent[ri] = rj
            self.N -= 1

def findCircleNum(M):
    N = len(M)
    uf = UF(N)
    for i in range(N):
        for j in range(i+1, N):
            if M[i][j] == 1:
                uf.union(i,j)

    return uf.N

M = [[1,1,0],[1,1,0],[0,0,1]]
print(findCircleNum(M))