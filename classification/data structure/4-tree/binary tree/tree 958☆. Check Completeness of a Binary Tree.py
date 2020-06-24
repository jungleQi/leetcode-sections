def isCompleteTree(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root: return True
    nodes = [(root, 1)]
    i = 0
    while i < len(nodes):
        node, v = nodes[i]
        i += 1
        if node.left:
            nodes.append((node.left, 2 * v))
        if node.right:
            nodes.append((node.right, 2 * v + 1))

    return nodes[-1][1] == i