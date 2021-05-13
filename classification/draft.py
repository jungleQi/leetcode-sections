import collections

def levelOrderBottom(root):
    levels = []
    if not root: return levels

    q = collections.deque([root])
    while q:
        N = len(q)
        level = []
        while N>0:
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            N -= 1

        levels.insert(0, level)
    return levels