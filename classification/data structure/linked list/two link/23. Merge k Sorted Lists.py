'''
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

from leetcode.classification.utils import *
def mergeKLists(lists):
    all_nodes = []
    for list in lists:
        while list:
            all_nodes.append(list)
            list = list.next

    all_nodes.sort(key=lambda x:x.val)
    head = cur = ListNode(-1)
    for i, node in enumerate(all_nodes):
        cur.next, cur = node, node
    return head.next

import heapq
def mergeKLists_heap(lists):
    heap = []
    for i, lt in enumerate(lists):
        if not lt: continue
        heapq.heappush(heap, [lt.val, lt])

    head = cur = ListNode(-1)
    while heap:
        minNode = heapq.heappop(heap)
        cur.next, cur = minNode[1], minNode[1]
        if cur.next:
            heapq.heappush(heap, [cur.next.val, cur.next])

    return head.next