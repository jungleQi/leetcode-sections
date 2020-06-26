def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """

    def helper(node):
        if not node: return False

        if p.val <= node.val and node.val <= q.val:
            ans[0] = node
            return True

        if helper(node.left): return True
        if helper(node.right): return True

        return False

    ans = [None]
    if p.val > q.val:
        p, q = q, p
    helper(root)
    return ans[0]
