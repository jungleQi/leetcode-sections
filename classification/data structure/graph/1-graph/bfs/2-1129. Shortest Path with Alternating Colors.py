#coding=utf-8

'''
Consider a directed graph, with nodes labelled 0, 1, ..., n-1.
In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.
Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of
the shortest path from node 0 to node X such that the edge colors alternate
along the path (or -1 if such a path doesn't exist).

Example 4:
Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]

Example 5:
Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]
'''

#dfs会遍历理论上所有的解空间递归子树，即便做了较好的pruing，也会在一些情况下有较差的性能
#bfs在解决一些最少递归层数的问题，有比较好的性能优势

import collections
def shortestAlternatingPaths_dfs_tle(n, red_edges, blue_edges):
    def travel(cur, prevColor, step):
        if ans[cur] == -1:
            ans[cur] = step
        else:
            ans[cur] = min(step, ans[cur])
        for idx, item in enumerate(graph[cur]):
            if visitor[cur][idx] or item[1] == prevColor:
                continue

            visitor[cur][idx] = True
            travel(item[0], item[1], step+1)
            visitor[cur][idx] = False

    graph = collections.defaultdict(list)
    for edge in red_edges:
        graph[edge[0]].append([edge[1],0])
    for edge in blue_edges:
        graph[edge[0]].append([edge[1], 1])

    #print graph[1]
    visitor = {}
    for key, val in graph.items():
        visitor[key] = [False]*len(val)

    ans = [-1]*n
    travel(0, -1, 0)
    return ans

def shortestAlternatingPaths_bfs(n, red_edges, blue_edges):
    graph = collections.defaultdict(list)
    for edge in red_edges:
        graph[edge[0]].append([edge[1],0])
    for edge in blue_edges:
        graph[edge[0]].append([edge[1], 1])

    visitor = {}
    for key, val in graph.items():
        visitor[key] = [False]*len(val)

    ans = [-1]*n
    deque = collections.deque([[0,-1,0]])
    while deque:
        item = deque.popleft()
        if ans[item[0]] == -1:
            ans[item[0]] = item[2]

        for idx, nei in enumerate(graph[item[0]]):
            if nei[1] != item[1] and not visitor[item[0]][idx]:
                deque.append(nei+[item[2]+1])
                visitor[item[0]][idx] = True

    return ans

n = 100
red_edges = [[23,30],[63,11],[92,53],[53,51],[74,47],[19,13],[25,67],[22,62],[15,57],[61,7],[84,11],[54,1],[1,67],[28,12],[93,3],[57,78],[43,17],[21,12],[48,30],[81,19],[76,11],[64,61],[37,3],[65,54],[81,73],[39,4],[29,64],[72,59],[37,49],[22,19],[52,66],[34,85],[62,29],[19,68],[43,74],[93,50],[91,22],[2,69],[6,9],[27,44],[19,41],[21,99],[18,96],[42,26],[88,38],[54,2],[31,60],[92,1],[12,49],[43,58],[31,37],[89,83],[15,42],[98,15],[96,26],[63,20],[54,47],[12,94],[10,7],[16,6],[14,17],[97,6],[6,28],[84,33],[17,83],[76,0],[29,14],[53,24],[61,41],[66,10],[2,37],[72,81],[85,47],[29,36],[94,24],[17,42],[53,80],[1,38],[56,49],[13,96],[64,9],[37,31],[45,31],[35,12],[91,80],[0,39],[38,41],[34,18],[36,8],[12,86],[9,83],[17,18],[31,16],[64,81],[17,17],[65,75],[32,93],[40,6],[8,28],[57,84],[24,87],[33,75],[86,38],[34,33],[79,40],[60,35],[99,79],[72,9]]
blue_edges = [[5,78],[33,51],[92,13],[32,15],[73,8],[40,41],[71,16],[86,47],[33,94],[57,44],[68,9],[89,52],[13,97],[40,15],[61,79],[51,2],[77,86],[66,24],[54,12],[42,92],[29,44],[11,55],[98,35],[63,59],[79,95],[33,90],[63,85],[78,10],[14,7],[8,36],[54,41],[95,74],[67,72],[83,87],[77,81],[66,43],[59,58],[34,19],[46,34],[24,3],[50,0],[47,83],[37,87],[92,92],[0,94],[25,2],[72,97],[79,24],[16,15],[31,33],[4,46],[65,63],[76,18],[64,89],[11,85],[68,62],[26,91],[47,75],[17,43],[70,22],[53,98],[55,39],[53,48],[45,51],[51,24],[79,50],[82,73],[27,26],[76,11],[1,50],[59,63],[42,78],[60,35],[47,51],[76,72],[96,35],[97,12],[87,6],[33,40],[15,35],[46,37],[57,59],[89,48],[3,27],[4,61],[34,40],[60,61],[32,43],[40,12],[60,23],[90,64],[81,75],[36,61],[47,73],[89,29],[34,78],[45,74],[75,13],[86,76],[13,93],[94,56],[93,91],[53,19],[95,6],[20,12],[2,45],[49,33],[20,78],[50,56],[79,14],[85,32],[65,45],[0,48],[81,82],[61,87],[50,15],[43,70],[86,38],[62,2],[89,97],[17,14],[52,2],[46,87],[0,16],[16,54],[86,5],[2,69],[80,77],[37,3],[89,59],[45,32],[47,17],[19,29],[69,81],[12,28],[52,73],[88,1],[10,92],[1,80],[21,57],[11,74],[19,25],[11,15],[25,29],[44,88],[86,13],[60,22],[97,55],[3,95],[73,51],[85,56],[58,97],[78,16],[42,84],[26,98],[46,10],[28,18],[14,12],[76,26],[79,12],[58,40],[72,89],[5,81],[41,65],[46,28],[18,25],[65,5],[0,85],[10,65],[28,56],[39,49],[22,17],[30,26],[53,6],[12,12],[16,16],[70,52],[96,55],[37,10],[72,15],[80,84],[50,60],[58,1],[76,74],[96,45],[42,77],[15,22],[99,19],[86,48],[98,11],[50,4],[71,44],[49,10],[4,31],[67,52],[52,94],[35,75],[83,63],[7,7],[99,38],[71,67],[18,84],[80,46],[80,15],[18,86],[10,75],[81,93],[67,31],[72,69],[18,24],[57,42],[93,8],[93,58]]
#n = 5
#red_edges = [[0,1],[1,2],[2,3],[3,4]]
#blue_edges =[[1,2],[2,3],[3,1]]
print shortestAlternatingPaths_bfs(n, red_edges, blue_edges)

