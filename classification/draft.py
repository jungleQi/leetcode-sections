#coding=utf-8

import heapq
def kthSmallest(matrix, k):
    heap = []
    cnt = 0
    M,N = len(matrix), len(matrix[0])
    for i in range(M):
        for j in range(N):
            if cnt < k:
                heapq.heappush(heap, -matrix[i][j])
            elif -matrix[i][j] > heap[0]:
                heapq.heapreplace(heap, -matrix[i][j])
            cnt += 1
    return -heap[0]

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print kthSmallest(matrix, k)


