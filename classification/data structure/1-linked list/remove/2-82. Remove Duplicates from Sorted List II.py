#coding=utf-8

'''
Given a sorted 1-linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Return the 1-linked list sorted as well.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
'''

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

#very wonderfull
#1.添加dummy，其值必须不同于第一个节点
#2.保证anchor节点值的唯一性，并且有效移动：
#  2.1 迭代比较，定位出等值节点区间尾部tail
#  2.2 如果遇到了等值区间(tail 存在移动，anchor.next != tail)，anchor保持不变，变的是anchor.next
#  2.3 如果没有遇到等值区间，anchor移动一次，变成anchor.next

def online_solution(head):
    dummy = ListNode()
    dummy.next = head
    anchor = dummy

    while anchor:
        cur = anchor.next
        while cur and cur.next and cur.val != cur.next.val:
            cur = cur.next

        if anchor.next != cur:
            anchor.next = cur.next
        else:
            anchor = anchor.next
    return dummy.next