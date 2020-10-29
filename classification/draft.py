class listNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

# 1 2 3 4 5 [ 2, 4]
def reverseBetween(head, m, n):
    dummy = listNode()
    dummy.next = head

    head = dummy
    i = 2
    while(head and i<=m):
        head = head.next
        i += 1

    tail = cur = head.next
    prev = None
    while(cur and m<=n):
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        m += 1

    head.next = prev
    tail.next = cur
    return dummy.next