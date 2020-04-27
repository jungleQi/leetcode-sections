#coding=utf-8
from utils import Node
from utils import ListNode
import heapq
import collections
#
#        p     c       n
#   N <- 1  <-   2     NULL
def reverseList(head):
    if not head or not head.next:
        return head

    ret = reverseList(head.next)
    head.next.next = head
    head.next = None
    return ret






