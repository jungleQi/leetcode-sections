'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
'''

#klogn
import heapq
def kthSmallest(matrix, k):
    heap = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            heapq.heappush(heap, -matrix[i][j])
            if len(heap) > k:
                heapq.heappop(heap)

    return -heap[0]

def kthSmallest(matrix, k):
    def push(i, j):
        if i < N and j < N:
            heapq.heappush(heap, [matrix[i][j], i, j])

    N = len(matrix)
    heap = []
    push(0, 0)
    pairs = set()
    x = 0

    while k > 0 and heap:
        x, i, j = heapq.heappop(heap)
        if (i + 1, j) not in pairs:
            push(i + 1, j)
            pairs.add((i + 1, j))
        if (i, j + 1) not in pairs:
            push(i, j + 1)
            pairs.add((i, j + 1))
        k -= 1
    return x

matrix = [[ 1,  5,  9],[10, 11, 13],[12, 13, 15]]
k = 9
print(kthSmallest(matrix, k))