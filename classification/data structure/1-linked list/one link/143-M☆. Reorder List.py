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
    def helper(prev, tail):
        # 为了对最终尾节点的next赋值None,从而防止环
        # 这里需要在head是最后一个节点时就返回，而不是为None时才返回，
        # 这样就无法为断后提供操作节点(tail.next == None)
        if not tail or not tail.next:
            return prev

        newHead = helper(prev, tail.next)
        #结束执行reorder的关键
        if not newHead or newHead == tail or not newHead.next:
            return None

        tmp = newHead.next
        newHead.next = tail.next
        tail.next.next = tmp
        tail.next = None #防止环

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


