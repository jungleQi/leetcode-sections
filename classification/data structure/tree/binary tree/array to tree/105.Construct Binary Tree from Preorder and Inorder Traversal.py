class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#O(N)
def buildTree(preorder, inorder):
    if not preorder or not inorder: return None

    curval = preorder[0]
    curidx = inorder.index(curval)

    root = TreeNode(curval)
    root.left = buildTree(preorder[1:curidx + 1], inorder[:curidx])
    root.right = buildTree(preorder[curidx + 1:], inorder[curidx + 1:])
    return root