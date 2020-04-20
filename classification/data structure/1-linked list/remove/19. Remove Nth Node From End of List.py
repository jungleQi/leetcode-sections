#coding=utf-8

'''
Given a 1-linked list, remove the n-th node from the end of list and return its head.

Example:

Given 1-linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the 1-linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''
from common import *

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#递归：1.递的路上处理问题；2.归的路上处理问题。这题是第二种情况

def removeNthFromEnd(head, n):
    if not head: return None

    lnode = ListNode(0)
    lnode.next = head

    def _helper(head):
        if not head:
            return 0

        endidx = _helper(head.next) + 1
        if endidx == n+1:
            head.next = head.next.next
        return endidx

    _helper(lnode)
    return lnode.next

values = []
head = constructlist(values)
ret = removeNthFromEnd(head, 0)
printList(ret)
