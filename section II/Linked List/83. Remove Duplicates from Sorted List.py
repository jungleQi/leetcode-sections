from common import *

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    ret = head
    while head:
        fastnode = head
        while fastnode.next and fastnode.val == fastnode.next.val:
            fastnode = fastnode.next
        head.next = fastnode.next
        head = fastnode.next

    return ret


values = [1,1,1,2,2,3,4,5,5]
head = constructlist(values)
ret = deleteDuplicates(head)
printList(ret)