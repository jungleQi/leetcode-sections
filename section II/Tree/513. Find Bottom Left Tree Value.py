'''
Given a binary tree, find the leftmost value in the last row of the tree.
'''
import common

def findBottomLeftValue(root):
    def _helper(node, level, leftmost):
        if node is None:
            return
        if not node.left and not node.right and level>leftmost[0]:
            leftmost[0], leftmost[1] = level, node.val
            return

        _helper(node.left, level+1, leftmost)
        _helper(node.right, level + 1, leftmost)

    leftmost = [1, root.val]
    _helper(root, 1, leftmost)
    return leftmost[1]

li = [1,2,3,4,4,None,5, None, None,6, None, 7]
tree = common.Tree()
tree.construct(li)
print(findBottomLeftValue(tree.root))