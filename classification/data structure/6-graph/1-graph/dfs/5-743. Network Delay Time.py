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

#坑：不能全部访问到了就返回TRUE，很有可能访问到了，但不是最短权值和，所以不能判断何时返回
#   而是一直遍历，直到每个点没有更小的权值和为止，这样效率确实比较低。
#1. dfs,避免不出现死循环，想用visitor来记录已经访问过的节点，如果已经访问过，就立即返回。
#   这样虽然避免了死循环，但是会误伤另外一条路径访问同一个节点时，可能耗时更短的可能

#key: 为了即不陷入graph的死循环，又不误伤到达同一节点的耗时更短路径，可以通过记录每个节点最小耗时。
#    如果当前路径耗时小于记录的最短耗时，就更新记录的最短耗时，继续dfs；否则就不做任何dfs处理，就此默认返回

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

