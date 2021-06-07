#coding=utf-8

'''
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
'''

def eraseOverlapIntervals_greedy(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    # 1.按照起始时间升序排列
    # 2.确定最近末端，如果当前起始时间小于末端，就要删除一个，并确定新的最小末端
    if not intervals: return 0

    intervals.sort(key=lambda x: x[0])
    minEnd = intervals[0][0]

    delCnt = 0
    for interval in intervals:
        if interval[0] >= minEnd:
            minEnd = interval[1]
            continue

        minEnd = min(interval[1], minEnd)
        delCnt += 1
    return delCnt

import heapq
def eraseOverlapIntervals_heap(intervals):
    heap = []
    res = 0
    for interval in sorted(intervals, key=lambda x:x[0]):
        if heap and interval[0] < -heap[0]:
            res += 1
            if interval[1] < -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -interval[1])
        else:
            heapq.heappush(heap, -interval[1])
    return res
