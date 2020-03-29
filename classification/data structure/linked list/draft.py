from utils import *

def middleNode(head):
    if not head or not head.next: return head

    slow, fast = head, head.next
    while fast:
        fast = fast.next
        if fast: fast = fast.next
        slow = slow.next
    return slow


arr = [1]
mylist = List(arr)
ret = middleNode(mylist.head)
print(ret.val)
#mylist.printList(ret)




