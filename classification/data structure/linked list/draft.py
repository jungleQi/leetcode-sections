from utils import *

def reorderList_recursion(head):
    def helper(prev, head):
        if not head or not head.next:
            return prev

        cur = helper(prev, head.next)
        if not cur or cur == head or not cur.next:
            return None

        tmp = cur.next
        cur.next = head.next
        head.next.next = tmp
        head.next = None

        return tmp

    helper(head, head)
    return head

def reorderList_interator(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    if head == None:
        return head
    temp = head
    k = 0
    nodes = list()
    while temp:
        nodes.append(temp)
        temp = temp.next

    prev = None
    for i in range((len(nodes) + 1) // 2):
        if prev:
            prev.next = nodes[i]
        nodes[i].next = nodes[-(i + 1)]
        prev = nodes[-(i + 1)]
    prev.next = None
    return prev

arr = [1,2,3]
mylist = List(arr)
ret = reorderList(mylist.head)
mylist.printList(ret)




