'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
'''

#Time complexity : O(N), where N is a number of nodes in the tree, since one visits each node exactly once

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(root1, root2):
    if not root1 or not root2:
        return root1 == root2

    if root1.val != root2.val:
        return False

    return isSameTree(root1.left, root2.left) and \
           isSameTree(root1.right, root2.right)
