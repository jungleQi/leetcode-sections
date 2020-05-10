#coding=utf-8

'''
Given a 1-linked list, remove the n-th node from the end of list and return its head.

Example:
Given 1-linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the 1-linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#递归：1.递的路上处理问题；2.归的路上处理问题。这题是第二种情况
# 返回的技巧是 (not curNode or not curNode.next)
# 递归之后接着就能处理当前node和其他node之间的关系
def removeNthFromEnd(head, n):
    def removeNode(curNode):
        if not curNode or not curNode.next:
            return 1

        ret = removeNode(curNode.next)
        if ret == n:
            curNode.next = curNode.next.next
        return ret + 1

    dummy = ListNode()
    dummy.next = head
    removeNode(dummy)
    return dummy.next

