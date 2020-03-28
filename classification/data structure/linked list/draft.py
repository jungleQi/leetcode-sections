from utils import *

def removeNthFromEnd(head, n):
    def helper(head):
        if not head:
            return 0
        ret = helper(head.next)
        if ret == n:
            head.next = head.next.next
        return ret + 1

    dummy = ListNode(-1)
    dummy.next = head
    helper(dummy)
    return dummy.next


arr = [1]
mylist = List(arr)
ret = removeNthFromEnd(mylist.head, 1)
mylist.printList(ret)




