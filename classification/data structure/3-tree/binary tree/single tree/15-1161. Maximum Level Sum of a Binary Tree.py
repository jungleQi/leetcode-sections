#coding=utf-8

'''
Given the root of a binary 3-tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
'''

def maxLevelSum(root):
    def travel(root, level, levels):
        if not root:
            return

        #处理层级问题的一个通用处理方式
        if len(levels) == level:
            levels.append(0)

        levels[level] += root.val
        travel(root.left, level + 1, levels)
        travel(root.right, level + 1, levels)

    levels = []
    travel(root, 0, levels)
    return levels.index(max(levels)) + 1
