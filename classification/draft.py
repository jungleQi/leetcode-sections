#coding=utf-8
from utils import Node
import heapq
import collections

def findOrder(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    indegree = [0]*numCourses

    for pre in prerequisites:
        graph[pre[1]].append(pre[0])
        indegree[pre[0]] += 1

    deque = collections.deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            deque.append(i)

    ans = []
    while deque:
        course = deque.popleft()
        ans.append(course)
        for nei in graph[course]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                deque.append(nei)

    return ans if len(ans) == numCourses else []


numCourses = 1
prerequisites = []
print findOrder(numCourses, prerequisites)