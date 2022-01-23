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
        # 为何贪婪的要删除掉最小(最左端)的，因为这样处理起来简单；
        # 也可以删除和当前interval[0]最左邻近的值，只是这样处理起来比较麻烦，还要拿着interval[0]去找比它小的最大那个值
        # 最后效果和直接删最小的值一样
        if heap and interval[0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])
    return len(heap)