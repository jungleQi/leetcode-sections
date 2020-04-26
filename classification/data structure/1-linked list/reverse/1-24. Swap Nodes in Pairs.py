'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
'''
from ....utils import ListNode

def swapPairs(head):
    dummy = ListNode(-1)
    prev = dummy
    prev.next = head

    while head and head.next:
        #reverse
        prev.next = head.next
        head.next = head.next.next
        prev.next.next = head
        #prepare for next reverse
        prev = head
        head = head.next
    return dummy.next
