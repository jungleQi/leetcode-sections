'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
'''

import common

def maxDepth(root):
    if not root: return 0
    return 1+max(map(maxDepth, [root.left, root.right]))


li = [3,9,20,None,None,15,7]
tree = common.Tree()
tree.construct(li)
ret = maxDepth(tree.root)
print(ret)