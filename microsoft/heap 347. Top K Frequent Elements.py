import collections,heapq
def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    counter = collections.Counter(nums)
    ret = heapq.nlargest(k, counter.keys(), key=counter.get)
    return ret