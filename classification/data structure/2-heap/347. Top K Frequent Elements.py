#coding=utf-8

'''
Given a non-empty 7-array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the 7-array's size.
'''

#2-heap.heapify 默认构建小顶堆

import collections,heapq
def topKFrequent(nums, k):
    counter = collections.Counter(nums)
    ret = heapq.nlargest(k, counter.keys(), key=counter.get)
    return ret

def topKFrequent_II(nums, k):
    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    h = []
    for key,val in counter.items():
        h.append((-val,key))

    heapq.heapify(h)
    ret = []
    for _ in range(k):
        ret.append(heapq.heappop(h)[1])
    return ret


nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent_II(nums, k))