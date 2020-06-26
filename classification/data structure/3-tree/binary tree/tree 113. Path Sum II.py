def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """

    def travel(root, path, k, ret):
        if (not root or (not root.left and not root.right)) and k == 0:
            ret.append(path)
            return
        if root.left:
            travel(root.left, path + [root.left.val], k - root.left.val, ret)
        if root.right:
            travel(root.right, path + [root.right.val], k - root.right.val, ret)

    ret = []
    if not root: return ret

    travel(root, [root.val], sum - root.val, ret)
    return ret