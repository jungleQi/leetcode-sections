class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    cur = head
    while cur and cur.next:
        newhead = cur.next.next

        #swap
        cur.next.next = cur
        prev.next = cur.next
        cur.next = newhead

        #prepare for next swap
        prev = cur
        cur = newhead

    return dummy.next