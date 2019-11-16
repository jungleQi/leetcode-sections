'''
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node,
any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.
Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

'''
import bisect

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bstFromPreorder(preorder):
    def _helper(i, j):
        if i == j:
            return None
        node = TreeNode(preorder[i])
        mid = bisect.bisect(preorder, preorder[i], i + 1, j)
        node.left = _helper(i + 1, mid)
        node.right = _helper(mid, j)
        return node

    return _helper(0, len(preorder))

