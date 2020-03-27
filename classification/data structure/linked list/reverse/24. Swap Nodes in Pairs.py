from ..utils import *

def swapPairs(head):
    dummy = ListNode(-1)
    prev = dummy
    prev.next = head

    while head and head.next:
        #reverse
        prev.next = head.next
        head.next = head.next.next
        prev.next.next = head
        #prepare for next reverse
        prev = head
        head = head.next
    return dummy.next


arr = [1,2,3,4]
mylist = List(arr)
ret = swapPairs(mylist.head)
mylist.printList(ret)