#coding=utf-8

'''
Reverse a linked list from position m to n. Do it in one-pass
Note: 1 ≤ m ≤ n ≤ length of list.
Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

#为了应对左端点被逆序，需要添加一个dummy头结点指向head，后面再怎么reverse，都只需要返回dummy.next
#沿用链表逆序的元组三变量(packing , unpacking)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseBetween(head, m, n):
    if m == n: return head

    dummy = ListNode()
    dummy.next = head
    head = dummy

    # 移动到m
    i = 1
    while i < m:
        head = head.next
        i += 1

    #关键控制性节点变量：
    #anchor 逆转区域前序节点，用于连接逆转之后的区域
    #newTail 逆转之后区域的尾结点
    #cur 初始化为待逆转区域的首节点
    anchor, newTail, cur = head, head.next, head.next

    #区域逆转
    prev = None
    while m <= n:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        m += 1

    #连接原始前部区域、逆转区域、原始后部区域
    anchor.next = prev
    newTail.next = cur

    return dummy.next


def reverseBetween_onepass(head, m, n):
    def travel(curnode, i):
        if i == n:
            return curnode, curnode.next

        #p,q 总是返回的第n个节点和n+1个节点，用于后面大结局时 三部分区域 的串联
        p, q = travel(curnode.next, i + 1)

        #reverse操作成功后，在归途中直接返回，不做任何处理
        if not p and not q:
            return None, None

        if i == m - 1:
            ###大结局
            curnode.next.next = q
            curnode.next = p
            return None, None

        ###reverse一次
        curnode.next.next = curnode
        curnode.next = None

        return p, q

    dummy = ListNode()
    dummy.next = head
    travel(dummy, 0)
    return dummy.next