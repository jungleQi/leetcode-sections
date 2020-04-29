'''
Given a sorted 1-linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

def deleteDuplicates_recursion(head):
    if not head or not head.next: return head

    if head.val == head.next.val:
        head.next = head.next.next
        deleteDuplicates_recursion(head)
    else:
        deleteDuplicates_recursion(head.next)

    return head