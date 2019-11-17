'''
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def allPossibleFBT(N):
    def _helper(N, cur, ret):
        if N == 0: return None
        root = TreeNode(0)
        if N == 3:
            root.left = TreeNode(0)
            root.right = TreeNode(0)
            return root

        root

