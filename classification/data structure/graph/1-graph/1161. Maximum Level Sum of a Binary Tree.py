'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
'''
from ....utils import ListNode
import collections
def maxLevelSum(root):
    def dfs(node, level):
        if not node: return
        levelSum[level] += node.val

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    levelSum = collections.defaultdict(int)
    dfs(root, 1)
    sumLevel = {}
    for level, num in levelSum.items():
        if num not in sumLevel:
            sumLevel[num] = [level]
        else:
            sumLevel[num].append(level)

    sortAns = sorted(sumLevel.items(), key=lambda x: x[0], reverse=True)
    sortAns[0][1].sort()
    return sortAns[0][1][0]
