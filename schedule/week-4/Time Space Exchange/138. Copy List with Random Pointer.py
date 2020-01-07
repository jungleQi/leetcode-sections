#coding=utf-8

'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
'''

#1.dict(hashmap)记录每个旧节点对象和新节点对象的对应关系；
#  然后遍历旧链表，根据映射关系，构建新链表的next和random pointer

#2.weaving法：
# 2.1 创建新节点A'将它插入A之后， 类似B'插入B之后，形成A->A'->B->B'...;
# 2.2 依据新的weaving链表，构建新插入节点的random pointer
# 2.3 将A->A'->B->B'分解成A->B, A'->B'，因为返回copy链表的同时，要保持原链表不变

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

#Time  Complexity : O(N)
#Space Complexity : O(N)
def copyRandomList(head):
    if not head: return head

    nodemap = dict()
    p = head
    while p:
        node = Node(p.val)
        nodemap[p] = node
        p = p.next

    newhead = q = nodemap[head]
    while head:
        if head.next:
            q.next = nodemap[head.next]
        if head.random:
            q.random = nodemap[head.random]
        q = q.next
        head = head.next
    return newhead


#Time  Complexity : O(N)
#Space Complexity : O(1)
def copyRandomList_weaving(head):
    if not head:
        return None

    ptr = head
    while ptr:
        node = Node(ptr.val)
        ptr.next, node.next = node, ptr.next
        ptr = node.next

    ptr = head
    while ptr:
        ptr.next.random = ptr.random.next if ptr.random else None
        ptr = ptr.next.next

    ptr_new_list = head.next
    ptr_old_list = head
    head_new = head.next
    while ptr_old_list:
        ptr_old_list.next = ptr_old_list.next.next
        ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
        ptr_old_list = ptr_old_list.next
        ptr_new_list = ptr_new_list.next

    return head_new

