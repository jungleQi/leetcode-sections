#coding=utf-8

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

#首先按照start进行升序排序，这是后面比较逻辑的基础
#需要每次和最小的end进行比较
# 1.如果当前interval.start大于之前最小end，说明可以共用一个room，最小的end就失效，新的end入堆
# 2.否则，没有可共用的room，需要新增一个room，新的end入堆
# 3.为什么如果当前interval start大于堆中多个interval-end时，选择拿当前的end替换掉堆顶最小的那个end，
#   而不是替换堆中和当前end最临近的那个值呢？因为当前的start大于堆中多个元素，后面interval的start也会大于
#   堆中多个元素，选择替换堆中的哪个元素最后结果都一样，只是替换堆顶元素操作起来会很简单
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