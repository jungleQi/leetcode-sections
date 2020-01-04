#coding=utf-8

'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeKLists(lists):
    def two_merge(l1, l2):
        prehead = ListNode(-1)
        pre = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next

        return prehead.next

    n = len(lists)
    newlist = two_merge(lists[0], lists[1])
    for i in range(2,n):
        newlist = two_merge(newlist, lists[i])
    return newlist

#elegant: 将每个node节点存入列表，node节点后续的next链条没必要特殊处理，挂着排序之后，重新连接时就会被断开
def mergeKLists_nlogn(lists):
    all_nodes = []
    for x in lists:
        while x:
            all_nodes.append(x)
            x = x.next

    all_nodes_sorted = sorted(all_nodes, key=lambda node: node.val)
    phead = ListNode(-1)
    p = phead
    for curnode in all_nodes_sorted:
        p.next = curnode
        p = p.next

    return phead.next