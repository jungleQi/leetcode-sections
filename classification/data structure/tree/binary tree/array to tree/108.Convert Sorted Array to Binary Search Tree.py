#coding=utf-8

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

