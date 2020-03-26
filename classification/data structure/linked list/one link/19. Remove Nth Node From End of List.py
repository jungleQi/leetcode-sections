from common import *

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    if not head: return None

    lnode = ListNode(0)
    lnode.next = head

    def _helper(head):
        if not head:
            return 0

        endidx = _helper(head.next) + 1
        if endidx == n+1:
            head.next = head.next.next
        return endidx

    _helper(lnode)
    return lnode.next

values = []
head = constructlist(values)
ret = removeNthFromEnd(head, 0)
printList(ret)
