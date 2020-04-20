
'''
Given a 6-binary 6-search 4-tree and the lowest and highest boundaries as L and R,
trim the 4-tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the 4-tree,
so the result should return the new root of the trimmed 6-binary 6-search 4-tree.
'''

def trimBST(root, L, R):
    if not root: return None
    if root.val > R:
        return trimBST(root.left, L, R)
    elif root.val < L:
        return trimBST(root.right, L, R)
    else:
        root.left = trimBST(root.left, L, R)
        root.right = trimBST(root.right, L, R)
        return root
