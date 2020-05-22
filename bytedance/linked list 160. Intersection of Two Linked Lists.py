#coding=utf-8

def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    #写个函数求链表长度
    def getlen(head):
        n = 0
        while head:
            n += 1
            head = head.next
        return n

    na, nb = getlen(headA), getlen(headB)
    if na > nb:
        while na != nb:
            headA = headA.next
            na -= 1
    else:
        while na != nb:
            headB = headB.next
            nb -= 1

    while headA != headB:
        headA = headA.next
        headB = headB.next
    return headA