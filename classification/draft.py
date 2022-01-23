import heapq

def findMinArrowShots(points):
    heap = []
    res = 0
    for pt in sorted(points, key=lambda x:x[0]):
        if heap and pt[0] > heap[0]:
            res += 1
            heapq.heappop(heap)
            heapq.heappush(heap, pt[1])
        else:
            if not heap:
                heapq.heappush(heap, pt[1])
                res += 1
            elif pt[1] < heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, pt[1])

    return res


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(findMinArrowShots(points))