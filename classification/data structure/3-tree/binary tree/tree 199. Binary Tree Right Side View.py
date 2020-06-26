def rightSideView(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    def helper(root, level, ret):
        if not root: return

        if len(ret) == level:
            ret.append(root.val)

        helper(root.right, level + 1, ret)
        helper(root.left, level + 1, ret)

    ret = []
    helper(root, 0, ret)
    return ret