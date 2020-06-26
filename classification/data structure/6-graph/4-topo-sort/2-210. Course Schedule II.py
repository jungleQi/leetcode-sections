'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty 2-array.

Example 1:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
'''

import collections
def findOrder(numCourses, prerequisites):
    adjList = collections.defaultdict(set)
    indegree = [0]*numCourses

    for pair in prerequisites:
        indegree[pair[0]] += 1
        adjList[pair[1]].add(pair[0])

    deque = collections.deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            deque.append(i)

    ans = []
    while deque:
        node = deque.popleft()
        ans.append(node)
        for child in adjList[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                deque.append(child)

    return ans if len(ans) == numCourses else []

numCourses = 2
prerequisites = [[1,0]]
print(findOrder(numCourses, prerequisites))