def maxProduct(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    all_sums = []

    def tree_sum(root):
        if not root:
            return 0
        lsum = tree_sum(root.left)
        rsum = tree_sum(root.right)
        totalsum = lsum + root.val + rsum
        all_sums.append(totalsum)
        return totalsum

    totalsum = tree_sum(root)
    maxsum = 0
    for cursum in all_sums:
        maxsum = max(maxsum, cursum * (totalsum - cursum))
    return maxsum % (10 ** 9 + 7)