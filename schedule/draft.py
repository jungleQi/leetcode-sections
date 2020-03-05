#coding=utf-8

class UF(object):
    def __init__(self):
        self.parent = dict()

    def find(self, x):
        #如果找到就得到，找不到就设置
        p,xr = self.parent.setdefault(x, (x, 1.0))
        if p != x:
            r, pr = self.find(p)
            self.parent[x] = r, pr*xr
        return self.parent[x]

    def union(self, x, y, load):
        px,xr = self.find(x)
        py,yr = self.find(y)
        if load:
            self.parent[px] = py, load*xr/yr
        else:
            return xr/yr if px == py else -1

def calcEquation(equations, values, queries):
    uf = UF()
    for (x,y), v in zip(equations, values):
        uf.union(x, y, v)

    return [uf.union(x,y,0) if x in uf.parent and y in uf.parent else -1.0 for x, y in queries]

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(calcEquation(equations, values, queries))