'''
Invert a binary 3-tree.
'''

#Since each node in the tree is visited only once, the time complexity is O(n),
# where n is the number of nodes in the tree.
# We cannot do better than that, since at the very least we have to visit each node to invert it.

def invertTree(root):
    if not root: return None
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root
