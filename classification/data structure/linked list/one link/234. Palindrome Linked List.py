#coding=utf-8

'''
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
'''

from common import *

def isPalindrome(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next
    return l == l[::-1]

#如果让头部节点在"归"的过程中，配合递归时逆向行驶的节点，做相向的移动，有两种方式：
#1. "递"结束之后，返回头部，每次"归"时，返回节点next
#2. 在递归函数之外，定义一个头部节点lnode，每次"归"时，lnode移动到next

def isPalindrome_recursive(head):
    def helper(e):
        if not e or not e.next:
            return head

        prev = helper(e.next)
        if not prev or prev.val != e.next.val:
            return None
        return prev.next

    if not head: return True
    ret = helper(head)
    return ret != None

class Solution(object):
    lnode = None

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True

        self.lnode = head
        return self._helper(head)

    def _helper(self, nod):
        if not nod.next:
            return self.lnode.val == nod.val

        res = self._helper(nod.next)
        self.lnode = self.lnode.next
        return res and self.lnode.val == nod.val