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

matrix = [[ 1,  5,  9],[10, 11, 13],[12, 13, 15]]
k = 9
print(kthSmallest(matrix, k))