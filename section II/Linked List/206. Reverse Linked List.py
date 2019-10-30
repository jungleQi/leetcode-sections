class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def constructlist(values):
    prevNode,head = None, None
    for v in values:
        if not prevNode:
            head = prevNode = ListNode(v)
        else:
            prevNode.next = ListNode(v)
            prevNode = prevNode.next

    return head

def printList(pHead):
    while pHead:
        print(pHead.val)
        pHead = pHead.next

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