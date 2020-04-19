#coding=utf-8

'''
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.
These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.
'''

#关键在于：
# 1.对每个 1 x 1 square 进行子区域划分，划分成4个
# 2.对划分的区域内部进行连通
# 3.对相邻square区域，两者之间相邻的1/4子区域进行连通
# 4.为了做好子区域连通，需要对每个square的4个子区域进行编号，编号从0开始递增到4*N*N

class DSU(object):
    def __init__(self, N):
        self.p = range(N)

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x] #不能返回x，不一样

    def union(self, x, y):
        xr = self.find(x)
        xy = self.find(y)
        self.p[xr] = xy

def regionsBySlashes(grid):
    N = len(grid)
    dsu = DSU(4*N*N)
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            root = 4*(r*N+c)
            if v in "/ ":
                dsu.union(root+0, root+1)
                dsu.union(root+2, root+3)
            if v in "\ ":
                dsu.union(root+1, root+2)
                dsu.union(root+0, root+3)

            if r+1 < N: dsu.union(root+3, (root+4*N) + 1)
            if r-1 >= 0: dsu.union(root+1, (root-4*N) + 3)
            if c+1 <N: dsu.union(root+2, (root+4)+0)
            if c-1 >= 0: dsu.union(root, (root-4)+2)

    return sum(dsu.find(i) == i for i in range(4*N*N))

grid = [" /","/ "]
print(regionsBySlashes(grid))