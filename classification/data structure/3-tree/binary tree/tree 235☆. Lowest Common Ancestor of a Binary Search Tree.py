def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """

    def helper(root, p, q, ret):
        if not root:
            return

        if root.val >= p.val and root.val <= q.val:
            ret[0] = root
            return
        elif root.val < p.val:
            helper(root.right, p, q, ret)
        elif root.val > q.val:
            helper(root.left, p, q, ret)

    ret = [None]
    if p.val > q.val:
        p, q = q, p
    helper(root, p, q, ret)
    return ret[0]