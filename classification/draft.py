#coding=utf-8
from utils import Node
from utils import ListNode
import heapq
import collections

# 1 ->  1   ->  2   ->  3   ->3   ->  4   ->  NULL
def deleteDuplicates(head):
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head