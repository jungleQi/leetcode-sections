'''
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

'''

import collections
def longestIncreasingPath(matrix):
    if not matrix: return 0

    # Step 1: build a directed acyclic graph
    graph = collections.defaultdict(list)
    indegree = collections.defaultdict(int)

    M,N = len(matrix), len(matrix[0])
    for i in range(M):
        for j in range(N):
            neigh = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
            for m,n in neigh:
                if m>=0 and m<M and n>=0 and n<N and matrix[i][j]<matrix[m][n]:
                    graph[(i,j)].append((m,n))
                    indegree[(m,n)] += 1

    # Step 2: Topological sorting with Kahn's algorithm
    queue = collections.deque([(i,j) for i in range(M) for j in range(N) if (i,j) not in indegree])
    maxlen = 0
    while queue:
        maxlen += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    queue.append(neigh)
    return maxlen

matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix))