import collections


def verticalOrder_bfs(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root: return []
    data = collections.defaultdict(list)
    deque = collections.deque([(root, 0)])

    while deque:
        node, col = deque.popleft()
        data[col].append(node.val)

        if node.left:
            deque.append((node.left, col - 1))
        if node.right:
            deque.append((node.right, col + 1))

    ret = sorted(data.items(), key=lambda x: x[0])
    return zip(*ret)[1]


def verticalOrder_dfs(root):
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