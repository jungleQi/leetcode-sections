def largestValues(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    def travel(root, level, ret):
        if not root: return

        if level == len(ret):
            ret.append([])

        ret[level].append(root.val)
        travel(root.left, level + 1, ret)
        travel(root.right, level + 1, ret)

    ret = []
    travel(root, 0, ret)

    ans = []
    for row in ret:
        ans.append(max(row))
    return ans