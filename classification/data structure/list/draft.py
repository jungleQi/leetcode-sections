from utils import *
def reverseList_iterator(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev

def reverseList_recursive(head):
    if not head or not head.next:
        return head

    p = reverseList_recursive(head.next)
    head.next.next = head
    head.next = None
    return p