'''
There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.
(A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities,
there exists a path of connections (possibly of length 1) that connects those two cities together.
The cost is the sum of the connection costs used. If the task is impossible, return -1.
'''

import collections
def minimumCost(N, connections):
    def travel(cur, cost):
        if sum(visitor.values()) == N:
            #print visitor, cost
            ret.append(cost)
            return

        for neighbor, curCost in graph[cur]:
            if visitor[neighbor]: continue
            visitor[neighbor] = True
            cost += curCost
            travel(neighbor, cost)
            #visitor[neighbor] = False

    graph = collections.defaultdict(list)
    for conn in connections:
        graph[conn[0]].append([conn[1],conn[2]])
        graph[conn[1]].append([conn[0],conn[2]])

    visitor = {city:False for city in range(1,N+1)}
    ret = []
    visitor[1] = True
    travel(1, 0)

    return min(ret) if ret else -1

N = 5
connections = [[2,1,50459],[3,2,47477],[4,2,52585],[5,3,16477]]
print(minimumCost(N, connections))
