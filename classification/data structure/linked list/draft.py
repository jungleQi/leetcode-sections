from utils import *
def reverseKGroup(head, k):
    def helper(cur, k):
        if k == 1:
            if not cur:
                return None, None
            else:
                return cur, cur.next

        if not cur or not cur.next:
            return None, None

        p,q = helper(cur.next, k - 1)
        if not p: return None, None

        cur.next.next = cur
        cur.next = None
        return p,q

    dummy = ListNode(-1)
    prev, dummy.next = dummy, head
    while True:
        p, q = helper(head, k)
        if not p: break
        prev.next, head.next = p, q
        prev, head = head, q

    return dummy.next


arr = [1,2,3,4,5]
mylist = List(arr)
ret = reverseKGroup(mylist.head, 5)
mylist.printList(ret)




