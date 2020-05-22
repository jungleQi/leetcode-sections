class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = ListNode()
    cur = dummy

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            cur = l1
            l1 = l1.next
        else:
            cur.next = l2
            cur = l2
            l2 = l2.next

    if l1:
        cur.next = l1
    else:
        cur.next = l2

    return dummy.next