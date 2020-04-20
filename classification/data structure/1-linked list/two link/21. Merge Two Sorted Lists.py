'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

from leetcode.classification.utils import *
def mergeTwoLists(l1, l2):
    head = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next, cur, l1 = l1, l1, l1.next
        else:
            cur.next, cur, l2 = l2, l2, l2.next
    cur.next = l1 if l1 else l2
    return head.next
