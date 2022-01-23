'''
There are some spherical balloons spread in two-dimensional space.
For each balloon, provided input is the start and end coordinates of the horizontal diameter.
Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice.
The start is always smaller than the end.

An arrow can be shot up exactly vertically from different points along the x-axis.
A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend.
There is no limit to the number of arrows that can be shot. An arrow once shot keeps traveling up infinitely.

Given an array points where points[i] = [xstart, xend],
return the minimum number of arrows that must be shot to burst all balloons.


Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
'''

def findMinArrowShots_greedy(points):
    if points == []:
        return 0

    #以x[1]为key进行升序排列
    points.sort(key=lambda x: x[1])
    arrows = 1

    currentEnd = points[0][1]
    for ballonStart, ballonEnd in points:
        if currentEnd < ballonStart:
            arrows += 1
            currentEnd = ballonEnd

    return arrows

def findMinArrowShots(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    # 以x[0]为key进行升序排列
    points.sort(key=lambda x: x[0])
    right = points[0][1]
    res = 1

    for pt in points[1:]:
        if pt[0] > right:
            res += 1
            right = pt[1]
        else:
            right = min(pt[1], right)
    return res

import heapq
def findMinArrowShots_heap(points):
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


points = [[1,9],[2,3],[5,10]]
print(findMinArrowShots_greedy(points))
print(findMinArrowShots_heap(points))