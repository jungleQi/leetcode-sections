#coding=utf-8

'''
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).
'''

#dfs并不是真的在遍历流程上实现了广度优先遍历，通过记录层数和列表的每层子列表个数， 而是在递归中确定将当前访问的节点值
# 追加到哪个层级的子列表

import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def levelOrder_dfs(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    levels = []
    if not root: return levels

    def _helper(node, level):
        if not node: return
        if len(levels) == level:
            levels.append([])

        levels[level].append(node.val)
        if node.left:
            _helper(node.left, level+1)
        if node.right:
            _helper(node.right, level+1)

    _helper(root, 0)
    return levels

def levelOrder_bfs(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    levels = []
    if not root: return levels

    q = collections.deque([root])
    while q:
        curCnt = len(q)
        level = []
        while curCnt > 0:
            node = q.popleft()
            curCnt -= 1
            level.append(node.val)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        levels.append(level)

    return levels