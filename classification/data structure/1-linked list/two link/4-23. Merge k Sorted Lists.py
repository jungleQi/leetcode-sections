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

from ....utils import *

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
    dummy = ListNode(0)
    head = dummy

    heap = []
    for i, l in enumerate(lists):
        if not l: continue
        heapq.heappush(heap, [l.val, l])
        lists[i] = l.next

    while heap:
        head.next = heapq.heappop(heap)[1]
        head = head.next

        if head.next:
            heapq.heappush(heap, [head.next.val, head.next])
    return dummy.next