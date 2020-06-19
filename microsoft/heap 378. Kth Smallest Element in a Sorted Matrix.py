import heapq
def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    heap = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            heapq.heappush(heap, -matrix[i][j])
            if len(heap) > k:
                heapq.heappop(heap)

    return -heap[0]