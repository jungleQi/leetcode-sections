from common import *

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

#very lower and rough
def deleteDuplicates(head):
    if not head : return None

    lnode = ListNode(head.val-1)
    lnode.next, curnode, remain_node = head, head, lnode

    isDup = False
    while curnode:
        if  curnode.next and curnode.val == curnode.next.val:
            curnode = curnode.next
            isDup = True
            continue

        if isDup:
            curnode = curnode.next
            remain_node.next = curnode
            isDup = False
        if not curnode: break

        if not curnode.next or curnode.val != curnode.next.val:
            remain_node.next = curnode
            remain_node = curnode
        else:
            isDup = True

        curnode = curnode.next

    return lnode.next

#very wonderfull
def online_solution(head):
    if not head or not head.next:
        return head
    curr = prev = ListNode(0)
    curr.next = head
    while (head and head.next):
        if head.val == head.next.val:
            while (head and head.next and head.val == head.next.val):
                head = head.next
            head = head.next
            prev.next = head
        else:
            prev = prev.next
            head = head.next
    return curr.next

values = [0,0,1,3,4,4,5,5,5]
nodes = online_solution(values)
ret = deleteDuplicates(nodes)
printList(ret)

