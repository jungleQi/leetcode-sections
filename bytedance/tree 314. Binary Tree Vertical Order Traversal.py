import collections
def verticalOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """

    def travel(node, vertical, level):
        if not node: return

        records[vertical].append([level, node.val])
        travel(node.left, vertical - 1, level + 1)
        travel(node.right, vertical + 1, level + 1)

    records = collections.defaultdict(list)
    travel(root, 0, 0)

    ret = sorted(records.items(), key=lambda x: x[0])
    ans = []
    for vert, leveldata in ret:
        curLevel = sorted(leveldata, key=lambda x: x[0])
        ans.append(zip(*curLevel)[1])
    return ans