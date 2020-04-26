#coding=utf-8
from utils import Node
from utils import ListNode
import heapq
import collections
#
# d -> 1    -> 2    ->    3  ->   4 ->  5   ->  NULL
# p   c     n  tmp
# x <- 1   2  -> 3
def reverseKGroup(head, k):
    def _reverse(_head, i):
        prev, cur, next = None, _head, _head.next
        while i > 0:
            cur.next = prev
            prev = cur
            cur = next
            next = next.next
            i -= 1
        return cur

    dummy = ListNode(0)
    dummy.next = head

    newHead = dummy
    while newHead:

        #judge if can reverse k nodes
        i = 1
        prob = newHead.next
        while i<k and prob:
            prob = prob.next
            i += 1
        if i != k: break

        #reverve k nodes
        tail = _reverse(newHead.next, i)
        tmp = newHead.next
        newHead.next.next  = prob
        newHead.next = tail
        newHead = tmp

    return dummy.next






