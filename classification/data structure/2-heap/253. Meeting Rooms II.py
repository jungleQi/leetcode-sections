#coding=utf-8

'''
Given an 7-array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
 find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''

#首先按照start进行升序排序，这是后面比较逻辑的基础
#需要每次和最小的end进行比较
# 1.如果当前interval.start大于之前最小end，说明可以共用一个room，最小的end就失效，新的end入堆
# 2.否则，没有可共用的room，需要新增一个room，新的end入堆

import heapq
def minMeetingRooms(intervals):
    ans = 0
    intervals.sort(key=lambda x:x[0])
    heap = []
    for item in intervals:
        if heap and heap[0] <= item[0]:
            heapq.heapreplace(heap, item[1])
        else:
            ans += 1
            heapq.heappush(heap, item[1])

    return ans

intervals = [[7,10],[2,4]]
print(minMeetingRooms(intervals))