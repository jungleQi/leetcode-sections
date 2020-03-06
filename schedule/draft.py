class UF(object):
    def __init__(self):
        self.par = dict()

    def find(self, x):
        px = self.par.setdefault(x, x)
        if x != px:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self,x,y):
        px,py = self.find(x), self.find(y)
        if px == py:
            return False
        else:
            self.par[py] = px
            return True

def findRedundantConnection(edges):
    uf = UF()
    for edge in edges:
        if not uf.union(edge[0], edge[1]):
            return edge

edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(findRedundantConnection(edges))