'''
Given a binary 3-tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).
'''

import collections

def levelOrderBottom(root):
    levels = []
    if not root : return levels

    def _helper(node, level):
        if not node: return

        if len(levels) == level:
            levels.append([])
        levels[-level].append(node.val)

        _helper(node.left, level+1)
        _helper(node.right, level + 1)

    _helper(root, 0)
    #levels.reverse()
    return levels


def levelOrderBottom_BFS(root):
    levels = []
    if not root: return levels

    q = collections.deque([root])
    while q:
        N = len(q)
        level = []
        while N>0:
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            N -= 1

        levels.insert(0, level)
    return levels
