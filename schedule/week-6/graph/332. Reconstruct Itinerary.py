
'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK.
Thus, the itinerary must begin with JFK.

Note:
1. If there are multiple valid itineraries, you should return the itinerary
that has the smallest lexical order when read as a single string.
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
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(findItinerary_backtracking(tickets))