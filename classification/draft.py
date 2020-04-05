#coding=utf-8

import collections
def numSquarefulPerms(A):
    graph = collections.defaultdict(list)
    count = collections.Counter(A)
    for x in count:
        for y in count:
            if int((x + y) ** .5 + 0.5) ** 2 == x + y:
                graph[x].append(y)

    N = len(A)

    def travel(n, path, ret):
        count[n] -= 1
        if len(path) == N:
            ret[0] += 1
        else:
            for nei in graph[n]:
                if count[nei] <= 0: continue
                travel(nei, path + [nei], ret)
        count[n] += 1

    ret = [0]
    for n in count:
        travel(n, [n], ret)
    return ret[0]