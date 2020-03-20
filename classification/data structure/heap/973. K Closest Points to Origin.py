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

#nlogn
def kClosest_ugly(points, K):
    dist = {}
    for pt in points:
        key = pt[0] * pt[0] + pt[1] * pt[1]
        if key not in dist:
            dist[key] = [pt]
        else:
            dist[key].append(pt)

    sortRet = sorted(dist.items(), key=lambda x:x[0])
    cnt = 0
    ret = []
    for item in sortRet:
        if cnt + len(item[1]) < K:
            ret += item[1],
            cnt += len(item[1])
        else:
            ret += item[1][:K-cnt],
            break

    return ret


def KClosest_slice(points, K):
    points.sort(key=lambda P: P[0] ** 2 + P[1] ** 2)
    return points[:K]


#n+klogn
import heapq
def kClosest_heapI(points, K):
    dist = []
    for pt in points:
        dist += (pt[0] * pt[0] + pt[1] * pt[1], pt),

    ans = []
    heapq.heapify(dist)
    for i in range(K):
        ans.append(heapq.heappop(dist)[1])

    return ans

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