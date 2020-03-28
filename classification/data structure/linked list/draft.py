from utils import *

def deleteDuplicates(head):
    if not head or not head.next: return head

    if head.val == head.next.val:
        head.next = head.next.next
        deleteDuplicates(head)
    else:
        deleteDuplicates(head.next)

    return head

arr = []
mylist = List(arr)
ret = deleteDuplicates(mylist.head)
mylist.printList(ret)




