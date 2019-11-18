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
    N -= 1
    if N == 0: return [TreeNode(0)]
    ret = []
    for i in range(1, N, 2):
        for left in allPossibleFBT(i):
            for right in allPossibleFBT(N - i):
                root = TreeNode(0)
                root.left = left
                root.right = right
                ret += [root]

    return ret



