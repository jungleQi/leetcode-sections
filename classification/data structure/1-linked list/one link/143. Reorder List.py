#coding=utf-8
'''
Given a singly 1-linked list L: L0->L1->..->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->..

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

from common import *

#如果是从尾部开始修改链表，多半是在 "归" 的路上处理节点
# 如果必要，需要递归返回下一个需要操作的节点
# 注意临界条件时的拦截返回
# 注意节点调整时，不要形成环

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

values = [1]
head = constructlist(values)
reorderList_recursion(head)
printList(head)


