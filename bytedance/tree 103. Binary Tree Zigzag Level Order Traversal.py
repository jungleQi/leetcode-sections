import collections
def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root: return []
    levels = []
    deque = collections.deque([(root, 0)])
    while deque:
        curnode, level = deque.popleft()
        if len(levels) == level:
            levels.append([])

        if level % 2 == 0:
            levels[level].append(curnode.val)
        else:
            levels[level].insert(0, curnode.val)

        if curnode.left:
            deque.append((curnode.left, level + 1))
        if curnode.right:
            deque.append((curnode.right, level + 1))

    return levels