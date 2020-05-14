#coding=utf-8

'''
Given an integer 7-array, return the k-th smallest distance among all the pairs.
The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
'''

#Time Complexity: O((k+N)logN), where N is the length of nums. As k = O(N^2),
# this is O(N^2*logN) in the worst case

#用堆会TLE，需要用二分+prefix sum

import heapq
def smallestDistancePair(nums, k):
    nums.sort()
    heap = [(nums[i + 1] - nums[i], i, i + 1) for i in xrange(len(nums) - 1)]
    heapq.heapify(heap)

    for _ in xrange(k):
        d, root, nei = heapq.heappop(heap)
        if nei + 1 < len(nums):
            heapq.heappush(heap, (nums[nei + 1] - nums[root], root, nei + 1))

    return d

# solved by Binary Search + Sliding Window