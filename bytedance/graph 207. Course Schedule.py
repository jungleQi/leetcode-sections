import collections
def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    graph = collections.defaultdict(list)
    indegree = collections.defaultdict(int)
    for pair in prerequisites:
        graph[pair[1]].append(pair[0])
        indegree[pair[0]] += 1

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

    return len(ans) == numCourses