class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if not preorder or not inorder:
        return None

    val = preorder[0]
    idx = inorder.index(val)
    root = TreeNode(val)

    root.left = buildTree(preorder[1:idx + 1], inorder[:idx])
    root.right = buildTree(preorder[idx + 1:], inorder[idx + 1:])
    return root