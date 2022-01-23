import collections


def zigzagLevelOrder_recursive(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    def helper(node, level):
        if not node: return

        if level == len(levels):
            levels.append([])

        if level % 2 == 0:
            levels[level].append(node.val)
        else:
            levels[level].insert(0, node.val)

        helper(node.left, level + 1)
        helper(node.right, level + 1)

    levels = []
    helper(root, 0)
    return levels

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