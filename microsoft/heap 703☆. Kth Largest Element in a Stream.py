import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.target = []

        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.target, val)

        if len(self.target) > self.k:
            heapq.heappop(self.target)
        return self.target[0]