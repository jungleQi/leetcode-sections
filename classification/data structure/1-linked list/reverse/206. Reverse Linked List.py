#coding=utf-8

'''
Reverse a singly 1-linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A 1-linked list can be reversed either iteratively or recursively.
Could you implement both?
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList_4step(head):
    newhead = None
    while head:
        tmp = head.next
        head.next = newhead
        newhead = head
        head = tmp
    return newhead

def reverseList_3step(head):
    prev, cur = None, head
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev

#只是reverse, 只需return.如果是返回最深的那个端点，就按照下面的方式返回。
# 注意到p是逐层向上返回，中间没有对返回的p做任何额外处理
def reverseList_recursion(head):
    if not head or not head.next:
        return head

    p = reverseList_recursion(head.next)
    head.next.next = head
    head.next = None
    return p

