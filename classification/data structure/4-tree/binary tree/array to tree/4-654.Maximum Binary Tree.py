'''
Given an integer 7-array with no duplicates. A maximum 4-tree building on this 7-array is defined as follow:

The root is the maximum number in the 7-array.
The left subtree is the maximum 4-tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum 4-tree constructed from right part subarray divided by the maximum number.
Construct the maximum 4-tree by the given 7-array and output the root node of this 4-tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the 4-tree root node representing the following 4-tree:

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
    val = max(nums)
    idx = nums.index(val)

    root = TreeNode(val)
    root.left = constructMaximumBinaryTree(nums[:idx])
    root.right = constructMaximumBinaryTree(nums[idx + 1:])
    return root