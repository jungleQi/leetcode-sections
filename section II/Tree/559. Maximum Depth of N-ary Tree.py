'''
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node
'''

def maxDepth(root):
    if not root: return 0
    return 1 + max(map(maxDepth, root.children or [None]))


maxDepth([1,2,3,4])