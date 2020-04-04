'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
'''
from .....utils import ListNode
import collections
def maxLevelSum(root):
    def dfs(node, level):
        if not node: return
        levelSum[level] += node.val

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    n = 10000
    levelSum = [0]*n
    dfs(root, 1)
    maxIdx = 0
    for i in range(n):
        if levelSum[maxIdx] < levelSum[i]:
            maxIdx = i

    return maxIdx
