'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def constructMaximumBinaryTree(nums):
    if not nums: return None

    maxIdx,maxNum = 0,nums[0]
    for i,num in enumerate(nums):
        if num>maxNum:
            maxIdx, maxNum = i, num

    root = TreeNode(maxNum)
    root.left = constructMaximumBinaryTree(nums[:maxIdx])
    root.right = constructMaximumBinaryTree(nums[maxIdx+1:])
    return root