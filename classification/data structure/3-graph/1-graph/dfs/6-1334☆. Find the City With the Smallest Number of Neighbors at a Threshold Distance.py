#coding=utf-8

'''
There are n cities numbered from 0 to n-1.
Given the 7-array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional
and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path
and whose distance is at most distanceThreshold, If there are multiple such cities,
return the city with the greatest number.

Notice that the distance of a path connecting cities i and j
is equal to the sum of the edges' weights along that path.

Example-1:

Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the 3-graph.
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1]
City 1 -> [City 0, City 4]
City 2 -> [City 3, City 4]
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3]
The city 0 has 1 neighboring city at a distanceThreshold = 2.
'''

import collections
def findTheCity(n, edges, distanceThreshold):
    def dfs(city, weight, cities):
        for nei in graph[city]:
            # if we have a condition on when to visit a node, then it would be better.
            # If you're visiting node A with a weight of 15 and if node A is already visited with a weight of 10 then,
            # it doesn't make sense to revisit node A. So maybe a visited with the least weight should work better
            if nei[1] + weight >= nodeweights[nei[0]] or nei[1] + weight > distanceThreshold:
                continue

            nodeweights[nei[0]] = nei[1] + weight
            cities.add(nei[0])
            dfs(nei[0], nei[1] + weight, cities)

    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append([edge[1], edge[2]])
        graph[edge[1]].append([edge[0], edge[2]])

    smallest, ans = n, 0
    for i in range(n):
        nodeweights = [float("inf")] * n

        #这里需要将[i]作为set的初始化，否则会出现 "坑" 下的BUG
        cities = set([i])

        dfs(i, 0, cities)
        if cities and len(cities) <= smallest:
            smallest = len(cities)
            ans = i
    return ans

#"坑"：
#input
# 4
# [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
# 4
#output
# 0 set([1, 2])
# 1 set([0, 1, 2, 3])
# 2 set([0, 1, 2, 3])
# 3 set([1, 2, 3])  <--3也在里面，导致输出 0 而不是3，所以需要在set([1, 2])中初始化0

n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4
print findTheCity(n, edges, distanceThreshold)

