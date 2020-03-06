
import collections
def findOrder(numCourses, prerequisites):
    indegree = [0]*numCourses
    graph = collections.defaultdict(list)

    for pair in prerequisites:
        indegree[pair[0]] += 1
        graph[pair[1]].append(pair[0])

    deque = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
    ret = []
    while deque:
        course = deque.popleft()
        ret.append(course)
        for nextCourse in graph[course]:
            indegree[nextCourse] -= 1
            if indegree[nextCourse] == 0:
                deque.append(nextCourse)

    return ret if len(ret) == numCourses else []

numCourses = 1
prerequisites = []
print(findOrder(numCourses, prerequisites))