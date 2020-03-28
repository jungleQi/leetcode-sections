from utils import *

def deleteDuplicates(head):
    if not head or not head.next:
        return head

    dummy = ListNode(head.val-1)
    dummy.next, cur = head, dummy
    while cur:
        tail = cur.next
        while tail and tail.next and tail.val == tail.next.val:
            tail = tail.next
        if cur.next != tail:
            cur.next = tail.next
        else:
            cur = cur.next

    return dummy.next

arr = []
mylist = List(arr)
ret = deleteDuplicates(mylist.head)
mylist.printList(ret)




