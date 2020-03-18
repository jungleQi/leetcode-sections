'''
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 <= k <= array's length.
'''

#nlogn
def findKthLargest_sort(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]

#nlogk
import heapq
def findKthLargest_heap(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for num in nums[k:]:
        if num>heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

    return heap[0]

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest_heap(nums, k))