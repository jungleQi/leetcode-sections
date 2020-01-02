#coding=utf-8

'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

#新建一个head node，prev指向 新链表的tail, 比较l1 和 l2，将小的node追加到tail，移动Prev 和l1 或者l2指针

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    if not l1 or not l2 or (l1.val>l2.val):
        return mergeTwoLists(l2, l1)

    h1,h2 = l1,l2
    while h1 and h2:
        if h1.next:
            if h1.val<=h2.val and h1.next.val>h2.val:
                next = h1.next
                h1.next = h2
                next2 = h2.next
                h2.next = next
                h2 = next2
            h1 = h1.next
        else:
            h1.next = h2

    return l1

def mergeTwoLists_iteration(l1, l2):
    prehead = ListNode(-1)

    pre = prehead
    while l1 and l2:
        if l1.val<=l2.val:
            pre.next = l1
            l1 = l1.next
        else:
            pre.next = l2
            l2 = l2.next
        pre = pre.next

    pre.next = l1 if not l2 else l2
    return prehead.next


