#coding=utf-8
'''
Given a singly 1-linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
'''

#如果让头部节点在"归"的过程中，配合递归时逆向行驶的节点，做相向的移动，有两种方式：
#1. "递"结束之后，返回头部，每次"归"时，返回节点next
#2. 在递归函数之外，定义一个头部节点lnode，每次"归"时，lnode移动到next


def isPalindrome_recursive(head):
    def helper(node, ret):
        if not node: return head

        newHead = helper(node.next, ret)
        if not newHead or newHead.val != node.val:
            ret[0] = False
            return None
        return newHead.next

    ret = [True]
    helper(head, ret)
    return ret[0]


def isPalindrome(head):
    l = []
    while head:
        l.append(head.val)
        head = head.next
    return l == l[::-1]