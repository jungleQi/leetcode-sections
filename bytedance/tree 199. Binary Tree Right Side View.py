def rightSideView(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    nodeLevel = {}

    def travel(curnode, level):
        if not curnode:
            return

        if level not in nodeLevel:
            nodeLevel[level] = curnode.val

        travel(curnode.right, level + 1)
        travel(curnode.left, level + 1)

    if not root: return []
    travel(root, 1)
    return zip(*sorted(nodeLevel.items(), key=lambda x: x[0]))[1]