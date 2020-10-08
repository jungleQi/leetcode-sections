'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1
'''

import heapq
def minMeetingRooms(intervals):
    intervals.sort(key=lambda x: x[0])

    heap = []
    for interval in intervals:
        if heap and interval[0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])
    return len(heap)