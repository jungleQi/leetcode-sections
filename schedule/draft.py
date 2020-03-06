import collections
def longestIncreasingPath(matrix):
    M,N = len(matrix), len(matrix[0])
    indegree = collections.defaultdict(int)
    graph = collections.defaultdict(list)

    for i in range(M):
        for j in range(N):
            neighbor = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            for m,n in neighbor:
                if m>=0 and m<M and n>=0 and n<N and matrix[m][n]>matrix[i][j]:
                    graph[(i, j)].append((m, n))
                    indegree[(m,n)] += 1

    deque = collections.deque([(i, j) for i in range(M) for j in range(N) if (i, j) not in indegree])
    maxLen = 0
    while deque:
        maxLen += 1
        for _ in range(len(deque)):
            i,j = deque.popleft()
            for item in graph[(i,j)]:
                indegree[item] -= 1
                if indegree[item]==0:
                    deque.append(item)
    return maxLen

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))
