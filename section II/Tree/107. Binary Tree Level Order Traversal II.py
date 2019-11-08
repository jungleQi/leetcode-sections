'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
 (ie, from left to right, level by level from leaf to root).
'''

import collections,common

def levelOrderBottom(root):
    def _helper(node, level, levelNode):
        if not node: return

        if level in levelNode.keys():
            levelNode[level].append(node.val)
        else:
            levelNode[level] = [node.val]

        _helper(node.left, level+1, levelNode)
        _helper(node.right, level + 1, levelNode)

    levelNode = collections.OrderedDict()
    _helper(root, 0, levelNode)
    ret = []
    for key, val in levelNode.items():
        ret.insert(0, val)
    return ret


li = [3]
tree = common.Tree()
tree.construct(li)
print(levelOrderBottom(tree.root))