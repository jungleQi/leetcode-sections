#coding=utf-8

'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w),
where u is the source node, v is the target node,
and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K.
How long will it take for all nodes to receive the signal? If it is impossible, return -1.

'''
#1. 对有向边进行 node : childList 的key map归类
#2. 进行dfs递归
#3. 每个节点dist[node]表示最小的到达时间，如果当前到达时间大于已有的到达时间，就返回；
# 否则更新为当前更小的到达时间

import collections

def networkDelayTime(times, N, K):
    graph = collections.defaultdict(list)
    for u,v,w in times:
        graph[u].append((v,w))

    dist = {node:float('inf') for node in range(1,N+1)}

    def dfs(elapse, node):
        if elapse>=dist[node]: return
        dist[node] = elapse
        for v,w in graph[node]:
            dfs(elapse+w, v)

    dfs(0, K)
    ans = max(dist.values())
    return ans if ans != float('inf') else -1

