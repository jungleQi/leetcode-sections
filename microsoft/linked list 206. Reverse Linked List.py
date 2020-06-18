def reverseList_iterative(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev, cur, next = None, head, None
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

def reverseList_recursive(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head

    ret = reverseList(head.next)
    head.next.next = head
    head.next = None
    return ret