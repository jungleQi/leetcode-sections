'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

from common import *

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    ret = head
    while head:
        fastnode = head
        while fastnode.next and fastnode.val == fastnode.next.val:
            fastnode = fastnode.next
        head.next = fastnode.next
        head = fastnode.next

    return ret

def deleteDuplicates_recursion(head):
    if not head or not head.next: return head

    if head.val == head.next.val:
        head.next = head.next.next
        deleteDuplicates_recursion(head)
    else:
        deleteDuplicates_recursion(head.next)

    return head

values = [1,1,1,2,2,3,4,5,5]
head = constructlist(values)
ret = deleteDuplicates(head)
printList(ret)