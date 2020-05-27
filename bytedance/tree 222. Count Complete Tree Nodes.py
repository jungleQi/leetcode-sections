def countNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def travel(node, ret):
        if not node:
            return
        ret[0] += 1

        travel(node.left, ret)
        travel(node.right, ret)

    ret = [0]
    travel(root, ret)
    return ret[0]