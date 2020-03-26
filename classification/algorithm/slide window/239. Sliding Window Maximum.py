'''
Given an array nums, there is a sliding window of size k which is moving from the very
left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position. Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
'''

# Keep indexes of good candidates in deque d. The indexes in d are from the current window,
# they're increasing, and their corresponding nums are decreasing.
# Then the first deque element is the index of the largest window value
#deque在窗口中的妙用，保持队列中的元素从头到尾是递减，即新来的元素淘汰掉队列尾部小于它的元素，最后新元素入队列

import collections
def maxSlidingWindow(nums, k):
    deq = collections.deque()
    out = []

    for i,n in enumerate(nums):
        while deq and nums[deq[-1]]<n:
            deq.pop()

        deq += i,
        if deq[0] == i-k:
            deq.popleft()
        if i>=k-1:
            out += nums[deq[0]],
    return out

nums = [1,3,-1,-3,5,3,6,7]
k = 8
print(maxSlidingWindow(nums, k))