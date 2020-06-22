def sumNumbers(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def travel(node, num, ret):
        if not node or (not node.left and not node.right):
            ret[0] += num
            return

        if node.left:
            travel(node.left, 10 * num + node.left.val, ret)
        if node.right:
            travel(node.right, 10 * num + node.right.val, ret)

    if not root: return 0

    ret = [0]
    travel(root, root.val, ret)
    return ret[0]