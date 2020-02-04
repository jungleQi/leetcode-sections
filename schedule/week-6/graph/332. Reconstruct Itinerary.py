
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

#tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
print(findItinerary(tickets))