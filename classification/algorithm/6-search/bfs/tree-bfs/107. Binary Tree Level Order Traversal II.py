'''
Given a binary 4-tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).
'''

def levelOrderBottom(root):
    levels = []
    if not root : return levels

    def _helper(node, level):
        if not node: return

        if len(levels) == level:
            levels.append([])
        levels[-level].append(node.val)

        _helper(node.left, level+1)
        _helper(node.right, level + 1)

    _helper(root, 0)
    #levels.reverse()
    return levels
