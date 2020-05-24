import heapq
def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    return heapq.nlargest(k, nums)[-1]