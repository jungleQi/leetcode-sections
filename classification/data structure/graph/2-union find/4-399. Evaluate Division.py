#coding=utf-8

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

#利用并查集，将所有equations中的pair，都计算它的分子、分母和根节点的除法结果
# 最后，以根节点为中间纽带，判断queries的分子分母分别和根节点的关系，从而得到他两之间的除值
def calcEquation_unionfind(equations, values, queries):
    parent = dict()

    #一般的 并查集find 直接将结果赋给parent
    #这个 需要得到返回的值，在返回值上做累积计算，再做赋值
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
            #注意分子分母不要颠倒
            parent[px] = (py, ry / rx * load)

    for (x, y), v in zip(equations, values):
        union(x, y, v)

    #如果if 带 else，就把判断放在for 之前,否则放在for之后
    return [union(x, y, 0) if x in parent and y in parent else -1.0 for x, y in queries]


equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(calcEquation_unionfind(equations, values, queries))