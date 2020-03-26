#coding=utf-8

'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

#新增链表头部的dummy(val:-1)
#判断剩余链表是否有K个节点，如果没有就退出循环
#元组三变量packing + unpacking
#最后如果还剩残余链表，将其接到前一个group子链表的尾部next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head, k):
    if k <= 1: return head

    dummy = ListNode(-1)
    dummy.next = head
    curtail = dummy

    while head:
        probe = head
        cnt = 0
        while probe and cnt < k:
            cnt += 1
            probe = probe.next

        if cnt != k: break

        i = 1
        prev, curhead = None, head
        while i <= k:
            head.next, prev, head = prev, head, head.next
            i += 1
        curtail.next = prev
        curtail = curhead
    if head: curtail.next = head
    return dummy.next
