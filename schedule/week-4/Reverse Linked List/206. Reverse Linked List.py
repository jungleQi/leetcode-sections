'''
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively.
Could you implement both?
'''

#

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

def reverseList_recursion(head):
    if not head or not head.next:
        return head

    p = reverseList_recursion(head.next)
    head.next.next = head
    head.next = None
    return p

