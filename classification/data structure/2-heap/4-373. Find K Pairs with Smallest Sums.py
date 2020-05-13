#coding=utf-8

'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first 7-array and one element from the second 7-array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

'''

import heapq
def kSmallestPairs(nums1, nums2, k):
    heap = []
    M, N = len(nums1), len(nums2)

    def push(i, j):
        if i < M and j < N:
            heapq.heappush(heap, [nums1[i] + nums2[j], i, j])

    pair = []
    push(0, 0)
    while k > 0 and heap:
        _, i, j = heapq.heappop(heap)
        pair.append([nums1[i], nums2[j]])
        #这是一组非常高明的选择Pair入堆过程！
        push(i, j + 1)
        if j == 0: # 防止同一pair重复入堆；当前较小的pair入堆
            push(i + 1, j)
        k -= 1
    return pair

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
print(kSmallestPairs(nums1, nums2, k))


