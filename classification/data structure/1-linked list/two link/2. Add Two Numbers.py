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

from utils import *
def addTwoNumbers(l1, l2):
    head = cur = ListNode(0)
    extra = 0
    while l1 or l2:
        if not l1 or not l2:
            if not l2:
                l2 , l1= l1, l2
            if l2.val + extra >= 10:
                val = l2.val + extra-10
                extra = 1
            else:
                val = l2.val + extra
                extra = 0
        else:
            if l1.val+l2.val+extra>=10:
                val = l1.val+l2.val+extra-10
                extra = 1
            else:
                val = l1.val+l2.val+extra
                extra = 0
            l1 = l1.next

        l2 = l2.next
        cur.next = ListNode(val)
        cur = cur.next

    if extra == 1:
        cur.next = ListNode(1)
    return head.next

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

arr1 = [0]
arr2 = [1,2]
l1, l2 = List(arr1), List(arr2)
ret = addTwoNumbers_recursion(l1.head, l2.head)

mylist = List(None)
mylist.printList(ret)
