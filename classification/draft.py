#coding=utf-8
from utils import Node
import heapq
import collections

def longestIncreasingPath(matrix):
    graph = collections.defaultdict(list)
    M,N = len(matrix), len(matrix[0])
    indegree = collections.defaultdict(int)
    for i in range(M):
        for j in range(N):
            if i > 0 and matrix[i][j]<matrix[i-1][j]:
                graph[(i,j)].append((i-1,j))
                indegree[(i-1,j)] += 1
            if j > 0 and matrix[i][j]<matrix[i][j-1]:
                graph[(i,j)].append((i, j-1))
                indegree[(i, j-1)] += 1
            if i < M-1 and matrix[i][j]<matrix[i+1][j]:
                graph[(i,j)].append((i+1,j))
                indegree[(i+1, j)] += 1
            if j < N-1 and matrix[i][j]<matrix[i][j+1]:
                graph[(i,j)].append((i,j+1))
                indegree[(i, j+1)] += 1
            if indegree[(i,j)] == 0:
                indegree[(i, j)] = 0

    deque = collections.deque()
    for coord, cnt in indegree.items():
        if cnt == 0:
            deque.append(coord)

    maxLen = 0
    while deque:
        maxLen += 1
        for i in range(len(deque)):
            cur = deque.popleft()
            for nei in graph[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    deque.append(nei)
    return maxLen


matrix = []
print longestIncreasingPath(matrix)
