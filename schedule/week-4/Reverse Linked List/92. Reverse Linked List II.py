#coding=utf-8

'''
Reverse a linked list from position m to n. Do it in one-pass
Note: 1 ≤ m ≤ n ≤ length of list.
Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

#为了应对左端点被逆序，需要添加一个dummy头结点指向head，后面再怎么reverse，都只需要返回dummy.next
#沿用链表逆序的元组三变量(packing , unpacking)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseBetween(head, m, n):
    if m == n: return head

    h1 = ret = ListNode(-1)
    ret.next = head
    i = 1
    while i < m:
        h1, head = head, head.next
        i += 1

    prev, cur = None, head
    while i <= n and cur:
        cur.next, prev, cur = prev, cur, cur.next
        i += 1
    if h1 and h1.next: h1.next.next = cur
    if h1: h1.next = prev

    return ret.next