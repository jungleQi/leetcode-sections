#coding=utf-8

'''
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
'''

#确定link list的中间节点或者是否有环，可以采用slow和fast，为了使处理简单：
#1.从同一个head节点出发，循环判断 fast and fast.next，循环体里进行各自的移动

def middleNode(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow