class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#inorder = [9,3,15,20,7]
#postorder = [9,15,7,20,3]

'''
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

def constructMaximumBinaryTree(nums):
    if not nums: return None

    idx = nums.index(max(nums))
    root = TreeNode(nums[idx])
    root.left = constructMaximumBinaryTree(nums[:idx])
    root.right = constructMaximumBinaryTree(nums[idx+1:])
    return root
