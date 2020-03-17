#coding=utf-8
'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(self, nums):
    if not nums: return None
    iroot = len(nums) // 2
    root = TreeNode(nums[iroot])
    root.left = self.sortedArrayToBST(nums[:iroot])
    root.right = self.sortedArrayToBST(nums[iroot + 1:])
    return root

