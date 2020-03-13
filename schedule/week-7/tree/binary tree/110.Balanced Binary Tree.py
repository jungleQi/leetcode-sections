'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.
'''


def isBalanced(root):
    def nodeDept(root):
        if not root: return 0
        dept = max(nodeDept(root.left), nodeDept(root.right)) + 1
        return dept

    if not root: return True
    delta = abs(nodeDept(root.left) - nodeDept(root.right))
    return delta < 2 and \
           isBalanced(root.left) and \
           isBalanced(root.right)
