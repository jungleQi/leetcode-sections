'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
'''

from collections import *

def canFinish_bfs(numCourses, prerequisites):
    forward = {i: set() for i in xrange(numCourses)}
    backward = defaultdict(set)
    for i, j in prerequisites:
        forward[i].add(j)
        backward[j].add(i)

    queue = deque([node for node in forward if len(forward[node]) == 0])
    while queue:
        node = queue.popleft()
        for neigh in backward[node]:
            forward[neigh].remove(node)
            if len(forward[neigh]) == 0:
                queue.append(neigh)
        forward.pop(node)
    return not forward  # if there is cycle, forward won't be None


def canFinish_dfs(numCourses, prerequisites):
    def _helper(graph, path, curkey):
        for v in graph[curkey]:
            if v in path: return False
            graph[curkey].remove(v)

            if not _helper(graph, path+[v], v): return False
        return True

    linkmap = defaultdict(list)
    for item in prerequisites:
        linkmap[item[0]].append(item[1])

    for k in linkmap.keys():
        if not _helper(linkmap, [k], k): return False

    return True


def canFinish_toposort(numCourses, prerequisites):
    edges = [[] for i in range(numCourses)]
    inDegree = [0 for i in range(numCourses)]

    for edge in prerequisites:
        inDegree[edge[0]] += 1
        edges[edge[1]].append(edge[0])

    q, count = deque(), 0

    for node in range(numCourses):
        if inDegree[node] == 0:
            q.append(node)

    while q:
        node = q.popleft()
        count += 1
        for neigh in edges[node]:
            inDegree[neigh] -= 1
            if inDegree[neigh] == 0:
                q.append(neigh)

    return count == numCourses


numCourses = 6
prerequisites = [[1,0],[0,5],[5,2],[1,3],[3,4],[4,5]]
print(canFinish_bfs(numCourses, prerequisites))