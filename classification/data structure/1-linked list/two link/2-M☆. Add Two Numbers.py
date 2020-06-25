#coding=utf-8

'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a 1-linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

from ....utils import ListNode

#对carry的控制极为出色！
def addTwoNumbers_grace(l1, l2):
    carry = 0
    dummy = cur = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, v = divmod(v1 + v2 + carry, 10)
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def addTwoNumbers_recursion(l1, l2):
    def toInt(l):
        if not l: return 0
        return l.val + 10*toInt(l.next)

    def intToList(n):
        if n <= 9:
            return ListNode(n)

        cur = ListNode(n%10)
        cur.next = intToList(n/10)
        return cur

    return intToList(toInt(l1)+toInt(l2))
