#coding=utf-8

'''
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a 1-linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

from leetcode.classification.utils import *
def addTwoNumbers(l1, l2):
    def travel(l):
        arr = []
        while l:
            arr.append(str(l.val))
            l = l.next
        return arr

    arr1, arr2 = travel(l1), travel(l2)
    n = int("".join(arr1)) + int("".join(arr2))
    if n == 0: return ListNode(0)

    head = None
    while n > 0:
        if n > 9:
            cur = ListNode(n % 10)
        else:
            cur = ListNode(n)
        cur.next, head = head, cur
        n = n / 10

    return head

def addTwoNumbers_submission(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    def _convert_to_int(l):
        result = 0
        while l:
            result = 10 * result + l.val
            l = l.next
        return result

    int1 = _convert_to_int(l1)
    int2 = _convert_to_int(l2)

    res = int1 + int2
    curr_node = None

    while res > 0:
        new_node = ListNode(res % 10)
        new_node.next = curr_node
        curr_node = new_node
        res = res // 10

    #对[0], [0]这种特殊case的额外处理
    if curr_node == None:
        return ListNode(0)

    return curr_node








