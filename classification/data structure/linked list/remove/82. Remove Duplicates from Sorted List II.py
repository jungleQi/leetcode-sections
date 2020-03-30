#coding=utf-8

'''
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
'''

from leetcode.classification.utils import *

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
#1.添加dummy，其值必须不同于第一个节点
#2.保证cur节点值的唯一性，并且有效移动：
#  2.1 迭代比较，定位出等值节点区间尾部tail
#  2.2 如果遇到了等值区间(tail 存在移动，cur.next != tail)，cur保持不变，变的是cur.next
#  2.3 如果没有遇到等值区间，cur移动一次，变成cur.next

def online_solution(head):
    if not head or not head.next:
        return head

    dummy = ListNode(head.val-1)
    dummy.next, cur = head, dummy
    while cur:
        tail = cur.next
        while tail and tail.next and tail.val == tail.next.val:
            tail = tail.next
        if cur.next != tail:
            cur.next = tail.next
        else:
            cur = cur.next

    return dummy.next

values = [0,0,1,3,4,4,5,5,5]
nodes = online_solution(values)
ret = deleteDuplicates(nodes)
printList(ret)

