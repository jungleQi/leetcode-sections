'''
Given the root of a binary tree, return the leftmost value in the last row of the tree.
'''

import collections
def findBottomLeftValue_BFS(root):
    q = collections.deque([root])
    while q:
        N = len(q)
        level = []
        while N>0:
            node = q.popleft()
            N -= 1
            level.append(node.val)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return level[0]



