#coding=utf-8
from utils import Node
from utils import ListNode
import heapq
import collections

# "abc3[cd]xyz"
def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    stack = [["", 0]]
    num = 0
    for c in s:
        if c.isdigit():
            num = 10 * num + int(c)
        elif c == '[':
            stack.append(["", num])
            num = 0
        elif c == ']':
            s, n = stack.pop()
            stack[-1][0] += s * n
        else:
            stack[-1][0] += c
    return stack[0][0]

print decodeString("3[a]2[bc]")