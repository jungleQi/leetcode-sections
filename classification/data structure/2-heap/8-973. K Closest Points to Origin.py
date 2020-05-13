'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)


Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
'''

def KClosest_slice(points, K):
    points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
    return points[:K]

import heapq
def KClosest_heapq(points, K):
    return heapq.nsmallest(K, points, key=lambda x: x[0] ** 2 + x[1] ** 2)

#nlogk
def kClosest_heapII(points, K):
    if len(points) <= K:
        return points

    heap = []
    for x,y in points:
        heapq.heappush(heap, [-(y ** 2 + x ** 2), [x, y]])
        if len(heap) > K:
            heapq.heappop(heap)

    return [p[1] for p in heap]


points = [[3,30],[5,-1],[-2,4],[4,-2]]
K = 2
print(kClosest_heapII(points, K))