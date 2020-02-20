'''
Equations are given in the format A / B = k, where A and B are variables represented as strings,
and k is a real number (floating point number).
Given some queries, return the answers. If the answer does not exist, return -1.0.
'''

import collections
def calcEquation(equations, values, queries):
    G = collections.defaultdict(dict)
    for (x,y), v in zip(equations, values):
        G[x][y] = v
        G[y][x] = 1/v

    def dfs(start, end, path, paths):
        if start == end and start in G:
            paths[0] = path
            return
        if start in seen:
            return

        seen.add(start)
        for node in G[start]:
            dfs(node, end, path*G[start][node], paths)

    ret = []
    for x, y in queries:
        paths, seen = [-1.0], set()
        dfs(x, y, 1.0, paths)
        ret.append(paths[0])
    return ret

def calcEquation_unionfind(equations, values, queries):
    parent = dict()

    def find(x):
        p, xr = parent.setdefault(x, (x, 1.0))
        if p != x:
            r, pr = find(p)
            parent[x] = r, pr * xr
        return parent[x]

    def union(x, y, load):
        (px, rx), (py, ry) = find(x), find(y)
        if not load:
            return rx / ry if px == py else -1.0
        if px != py:
            parent[px] = (py, ry / rx * load)

    for (x, y), v in zip(equations, values):
        union(x, y, v)

    return [union(x, y, 0) if x in parent and y in parent else -1.0 for x, y in queries]


equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(calcEquation_unionfind(equations, values, queries))