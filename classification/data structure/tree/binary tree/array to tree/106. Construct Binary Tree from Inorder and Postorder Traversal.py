class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#time complex: O(N)
def buildTree(inorder, postorder):
    if not inorder or not postorder: return None

    curval = postorder[-1]
    curidx = inorder.index(curval)

    root = TreeNode(curval)
    root.left = buildTree(inorder[:curidx], postorder[:curidx])
    root.right = buildTree(inorder[curidx + 1:], postorder[curidx:-1])
    return root