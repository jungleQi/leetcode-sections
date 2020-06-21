import heapq
def minMeetingRooms(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals.sort(key=lambda x: (x[0], x[1]))
    heap = []
    for interval in intervals:
        if heap and interval[0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, interval[1])
    return len(heap)