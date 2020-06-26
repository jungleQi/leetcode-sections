#coding=utf-8

'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
Thus, the itinerary must begin with JFK.

Note:
1. If there are multiple valid itineraries, you should return the itinerary
that has the smallest lexical order when read as a single 5-string.
For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
2.All airports are represented by three capital letters (IATA code).
3.You may assume all tickets form at least one valid itinerary.

Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
'''

import collections

def findItinerary(tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    def dfs(graph, source, res):
        while graph[source]:
            v = graph[source].pop()
            dfs(graph, v, res)
        res.append(source)

    graph = collections.defaultdict(list)
    for frm, to in tickets:
        graph[frm].append(to)
    for frm, tos in graph.items():
        tos.sort(reverse=True)
    res = []

    dfs(graph, "JFK", res)
    return res[::-1]

#坑：为了防止双向往返导致递归死循环，visitor记录访问过的路径[from, to]，如果该路径已经访问过，就不再继续递归下去，直接返回
#但是，同一个[from, to]可能会出现两次，这种记录就有问题，会让第二次正常的访问无法实现。

#1.建立好每个出发点的邻接表
#2.对Toes进行排序，并设定from到每个to的初始访问状态
#3.递归访问，构建解空间树，对每个to构建访问分支，并设立pruning判断
#4.当前路径长度等于预期路径长度，就保存结果并返回True.递归返回是True，就层层向上返回True

def findItinerary_backtracking(tickets):
    def backtracking(origin, path, result):
        if len(path) == flightNum + 1:
            result.append(path)
            return True

        for i, arrive in enumerate(flight[origin]):
            if not visitorMap[origin][i]:
                visitorMap[origin][i] = True
                ret = backtracking(arrive, path + [arrive], result)
                visitorMap[origin][i] = False
                if ret: return True
        return False

    path = ['JFK']
    if not tickets: return path
    flight = collections.defaultdict(list)
    for ticket in tickets:
        flight[ticket[0]].append(ticket[1])

    visitorMap = {}
    for depts, arrives in flight.items():
        arrives.sort()
        visitorMap[depts] = [False] * len(arrives)

    flightNum = len(tickets)
    result = []

    backtracking('JFK', path, result)
    return result[0]

#tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
print(findItinerary_backtracking(tickets))