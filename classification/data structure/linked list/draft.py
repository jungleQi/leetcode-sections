from utils import *

def sortList(head):
    curr = head
    l = []
    while curr is not None:
        l.append(curr.val)
        curr = curr.next
    l.sort()
    i = 0
    curr = head
    while i < len(l):
        curr.val = l[i]
        curr = curr.next
        i = i + 1
    return head

arr = [4,2,1,3]
mylist = List(arr)
ret = sortList(mylist.head)
mylist.printList(ret)




