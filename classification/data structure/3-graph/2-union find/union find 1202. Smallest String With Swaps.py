import collections
class UnionFind(object):
    def __init__(self, N):
        self.parent = range(N)
        self.unions = collections.defaultdict(set)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        ri, rj = self.find(i), self.find(j)
        self.parent[ri] = rj

    def cluster(self, N):
        for i in range(N):
            ri = self.find(i)
            self.unions[ri].add(i)
        return self.unions

def smallestStringWithSwaps(s, pairs):
    N = len(s)
    uf = UnionFind(N)
    for pair in pairs:
        uf.union(pair[0], pair[1])

    uf.cluster(N)
    dst = [""]*N
    for key, ids in uf.unions.items():
        strs = []
        for idx in ids:
            strs.append(s[idx])

        strs.sort()
        idlist = sorted(list(ids))

        for i,idx in enumerate(idlist):
            dst[idx] = strs[i]

    return "".join(dst)

s = "c"
pairs = []
print smallestStringWithSwaps(s, pairs)
