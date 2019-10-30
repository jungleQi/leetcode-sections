

def reverseList(head):
    prev = None
    cur, next = head, head.next
    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

def reverseList_recursive(head):
    if not head or not head.next:
        return head;

    p = reverseList_recursive(head.next)
    head.next.next = head
    head.next = None
    return p;

values = [1,3]
head = constructlist(values)
ret = reverseList_recursive(head)
printList(ret)