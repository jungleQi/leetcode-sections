def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None

    l = invertTree(root.left)
    r = invertTree(root.right)
    root.left = r
    root.right = l

    return root