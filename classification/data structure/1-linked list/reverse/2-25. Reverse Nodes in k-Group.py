#coding=utf-8

'''
Given a 1-linked list, reverse the nodes of a 1-linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the 1-linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this 1-linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

#1.新增链表头部的dummy(val:-1)
#2.判断剩余链表是否有K个节点，如果没有就退出循环
#3.选定[head, tail]区域进行reverse，注意迭代过程后，对结果的合法性检查：
#   if i < k or not tail 合法之后才进行该区域的reverse
#4.最后进行三个区域的串联（已reversed 刚reversed 未reversed）

#关键控制变量：
# 锚点anchor，用于串联reverse之后的[head, tail]区域
# tailnext，用于串联调整好的链表 和 tail之后待处理的子链表


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseKGroup(head, k):
    def reverse(cur, tail):
        if cur == tail: return
        reverse(cur.next, tail)
        cur.next.next = cur
        cur.next = None

    if k <= 1: return head

    dummy = ListNode()
    dummy.next = head
    anchor = dummy
    while anchor:
        tail = anchor.next
        i = 1
        while i < k and tail:
            tail = tail.next
            i += 1
        if i < k or not tail: break

        tailnext = tail.next
        newanchor = anchor.next

        reverse(anchor.next, tail)

        anchor.next.next = tailnext
        anchor.next = tail

        anchor = newanchor
    return dummy.next

#递归方式可以做到 one-pass
#每次递归逆转K个节点，两个关键点：
# 1.递归函数在访问完k-1个节点后，正常情况下返回最后一个节点和后续节点便于逆转和为下一段逆转做准备
# 2.递归函数返回值在返回时，只是层层向上返回，中间不做任何处理，保证能得到想要的第K个结点
# 3.循环依次逆转K个节点，直到最后发现没有k个节点作为一组了，就结束循环返回结果
def reverseKGroup_recursion(head, k):
    def helper(cur, k):
        if k == 1:
            if not cur:
                return None, None
            else:
                return cur, cur.next

        if not cur or not cur.next:
            return None, None

        p,q = helper(cur.next, k - 1)
        if not p: return None, None

        cur.next.next = cur
        cur.next = None
        return p,q

    dummy = ListNode(-1)
    prev, dummy.next = dummy, head
    while True:
        p, q = helper(head, k)
        if not p: break
        prev.next, head.next = p, q
        prev, head = head, q

    return dummy.next
