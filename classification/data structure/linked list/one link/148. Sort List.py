#coding=utf-8

'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''
from common import *

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def sortList(head):
    def merge(head1, head2):
        dummy = ListNode(0)
        e = dummy

        while head1 or head2:
            if head1 and (head2==None or head1.val<=head2.val):
                e.next = head1
                e = e.next
                head1 = head1.next

            if head2 and (head1==None or head2.val<head1.val):
                e.next = head2
                e = e.next
                head2 = head2.next

        return dummy.next

    if (not head) or (not head.next):
        return head

    slow_node = head
    fast_node = head.next
    while fast_node and fast_node.next:
        fast_node = fast_node.next.next
        slow_node = slow_node.next

    headb = slow_node.next
    slow_node.next = None

    return merge(sortList(head), sortList(headb))

#list sort 或者merge的问题，转换成arr，然后排序，是一种简洁的方法
def sortList_arr(head):
    l = []
    cur = head
    while cur:
        l.append(cur.val)
        cur = cur.next

    l.sort()
    i = 0
    cur = head
    while cur:
        cur.val = l[i]
        cur = cur.next
        i += 1
    return head

values = [1,1,1,2,2,3,4,5,5]
#values = [4,19,14,5,-3,1,8,5,11,15]
head = constructlist(values)
ret = sortList_arr(head)
printList(ret)