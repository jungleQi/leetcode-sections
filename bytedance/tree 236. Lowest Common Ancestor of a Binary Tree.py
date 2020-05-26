def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    ret = [None]

    def helper(root):
        if not root or ret[0]:
            return False

        mid = (root == p or root == q)
        lFound = helper(root.left)
        rFound = helper(root.right)
        if mid + lFound + rFound >= 2:
            ret[0] = root
            return False
        return mid or lFound or rFound

    helper(root)
    return ret[0]