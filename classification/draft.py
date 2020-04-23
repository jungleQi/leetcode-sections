#coding=utf-8
from utils import Node
from utils import ListNode
import heapq
import collections

#1.怎么使初始对象，随着递归而更新
# 1.1 作为递归函数的形参好像不行
# 1.2 在外部主函数声明，在递归函数内部更新，好像也不行
# 1.3

def isPalindrome(head):
    def helper(cur):
        if not cur or not cur.next:
            return head

        curHead = helper(cur.next)
        if not curHead  or curHead.val != cur.next.val:
            return None
        return curHead.next

    return helper(head) != None