from common import *

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    lnode = ListNode(0)
    lnode.next = head

    curnode = lnode
    while curnode.next and curnode.next.next:
        tmp1 = curnode.next.next.next
        tmp2 = curnode.next
        curnode.next = curnode.next.next
        curnode.next.next = tmp2
        tmp2.next = tmp1
        curnode = curnode.next.next

    return lnode.next

values = [1]
head = constructlist(values)
ret = swapPairs(head)
printList(ret)


