#coding=utf-8

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    #1.逆转
    def reverse(head, tail):
        prev, cur, next = None, head, None
        while cur and prev != tail:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return cur

    dummy = ListNode()
    dummy.next = head
    anchor = dummy
    while anchor:
        #定位逆转区间
        i, cur = k, anchor.next
        while i > 1 and cur:
            cur = cur.next
            i -= 1
        if not cur: break

        #逆转
        tail = reverse(anchor.next, cur)

        #串联该次区间逆转，为下次区间逆转做准备
        newhead = anchor.next
        anchor.next = cur
        newhead.next = tail
        anchor = newhead

    return dummy.next