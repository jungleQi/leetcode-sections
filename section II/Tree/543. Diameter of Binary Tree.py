'''
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.
'''

import common
global maxPath
maxPath = 0
def diameterOfBinaryTree(root):
    def _helper(node):
        global maxPath

        if node is None: return 0

        leftDept = _helper(node.left)+1 if node.left else 0
        rightDept = _helper(node.right)+1 if node.right else 0
        nodeDept = max(leftDept,rightDept)
        maxPath = max(maxPath, leftDept+rightDept)
        return nodeDept

    _helper(root)
    return maxPath

li = [1,2,None,3]
tree = common.Tree()
tree.construct(li)
print(diameterOfBinaryTree(tree.root))