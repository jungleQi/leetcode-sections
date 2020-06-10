#coding=utf-8

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    def convert2int(l):
        numArr = []
        while l:
            numArr.insert(0, str(l.val))
            l = l.next
        return int("".join(numArr))

    n = convert2int(l1) + convert2int(l2)
    dummy = ListNode()

    #处理[0],[0]的 corner case
    if n == 0:
        return dummy

    cur = dummy
    while n:
        cur.next = ListNode(n % 10)
        cur = cur.next
        n = n / 10
    return dummy.next