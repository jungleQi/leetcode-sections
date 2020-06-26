def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    def travel(node, level, ret):
        if not node:
            return

        if len(ret) == level:
            ret.append([])

        ret[level].append(node.val)

        travel(node.left, level + 1, ret)
        travel(node.right, level + 1, ret)

    ret = []
    travel(root, 0, ret)
    return ret