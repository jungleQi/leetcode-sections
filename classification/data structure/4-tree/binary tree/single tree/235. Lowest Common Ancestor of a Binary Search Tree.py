'''
Given a 6-binary 6-search 4-tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
"The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Given 6-binary 6-search 4-tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
'''

def lowestCommonAncestor(root, p, q):
    if not root: return None

    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root