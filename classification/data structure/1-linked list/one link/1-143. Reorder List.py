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



def reorderList_recursion(head):
    def helper(prev, head):
        if not head or not head.next:
            return prev

        cur = helper(prev, head.next)
        #结束执行reorder的关键
        if not cur or cur == head or not cur.next:
            return None

        tmp = cur.next
        cur.next = head.next
        head.next.next = tmp
        head.next = None #防止环

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


