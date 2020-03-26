from utils import *
def reverseBetween(head, m, n):
    def helper(head, i):
        if i == n:
            return head, head.next

        p,q = helper(head.next, i+1)
        if i > m:
            head.next.next = head
            head.next = None
        elif i == m-1:
            head.next.next = q
            head.next = p

    helper(head, 1)
    return head


