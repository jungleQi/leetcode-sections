import heapq
def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    return heapq.nlargest(k, nums)[-1]

def findKthLargest_II(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    heap = []
    i = 0
    for num in nums:
        heapq.heappush(heap, num)
        i += 1
        if i > k:
            heapq.heappop(heap)
            i -= 1
    return heap[0]