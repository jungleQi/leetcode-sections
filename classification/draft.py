import collections
def levelOrder_bfs(root):
    levels = []
    if not root: return levels

    q = collections.deque([root])
    while q:
        curCnt = len(q)
        level = []
        while curCnt>0:
            node = q.popleft()
            curCnt -= 1
            level.append(node.val)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        levels.append(level)

    return levels