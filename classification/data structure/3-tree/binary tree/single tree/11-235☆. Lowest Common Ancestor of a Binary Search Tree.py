'''
Given a 6-binary 6-search 3-tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
"The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Given 6-binary 6-search 3-tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
'''


def lowestCommonAncestor(root, p, q):
    def travel(root, p, q, ret):
        if not root: return

        if root.val >= p.val and root.val <= q.val:
            ret[0] = root
        elif root.val < p.val:
            travel(root.right, p, q, ret)
        elif root.val > q.val:
            travel(root.left, p, q, ret)

    ret = [None]
    if p.val > q.val:
        p, q = q, p
    travel(root, p, q, ret)
    return ret[0]

def lowestCommonAncestor_concise(root, p, q):
    if not root: return None

    if root.val > p.val and root.val > q.val:
        return lowestCommonAncestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root