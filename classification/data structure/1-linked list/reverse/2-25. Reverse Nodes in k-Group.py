#coding=utf-8

'''
Given a 1-linked list, reverse the nodes of a 1-linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the 1-linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this 1-linked list: 1->2->3->4->5

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

#递归方式可以做到 one-pass
#每次递归逆转K个节点，两个关键点：
# 1.递归函数在访问完k-1个节点后，正常情况下返回最后一个节点和后续节点便于逆转和为下一段逆转做准备
# 2.递归函数返回值在返回时，只是层层向上返回，中间不做任何处理，保证能得到想要的第K个结点
# 3.循环依次逆转K个节点，直到最后发现没有k个节点作为一组了，就结束循环返回结果
def reverseKGroup_recursion(head, k):
    def helper(cur, k):
        if k == 1:
            if not cur:
                return None, None
            else:
                return cur, cur.next

        if not cur or not cur.next:
            return None, None

        p,q = helper(cur.next, k - 1)
        if not p: return None, None

        cur.next.next = cur
        cur.next = None
        return p,q

    dummy = ListNode(-1)
    prev, dummy.next = dummy, head
    while True:
        p, q = helper(head, k)
        if not p: break
        prev.next, head.next = p, q
        prev, head = head, q

    return dummy.next
