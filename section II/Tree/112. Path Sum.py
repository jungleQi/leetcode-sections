'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.
'''

import common

global existSum
existSum = False
def hasPathSum(root, sum):
    def _helper(node, cursum):
        global existSum

        if node is None: return

        cursum += node.val
        if node.left is None and node.right is None and cursum == sum:
            existSum = True
            return

        if existSum: return

        _helper(node.left,  cursum)
        _helper(node.right, cursum)

    _helper(root,0)
    return existSum

li = [5,4,8,11,None,13,4,7,2,None,None,None,1]
tree = common.Tree()
tree.construct(li)
print(hasPathSum(tree.root, 26))


