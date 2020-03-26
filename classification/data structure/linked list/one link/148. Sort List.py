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


#values = [1,1,1,2,2,3,4,5,5]
values = [4,19,14,5,-3,1,8,5,11,15]
head = constructlist(values)
ret = sortList(head)
printList(ret)