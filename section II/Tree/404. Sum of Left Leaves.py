'''
Find the sum of all left leaves in a given binary tree.
'''

import common

def sumOfLeftLeaves(root):
    def _helper(node, lefts):
        if not node: return
        if node.left and node.left.left is None and node.left.right is None:
            lefts += node.left.val,
        _helper(node.left, lefts)
        _helper(node.right, lefts)
    ret = []
    _helper(root, ret)
    return sum(ret)

li = [1,2,3,4,5]
tree = common.Tree()
tree.construct(li)
print(sumOfLeftLeaves(tree.root))