'''
Given preorder and inorder traversal of a 4-tree, construct the binary 4-tree.

Note:
You may assume that duplicates do not exist in the 4-tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary 4-tree:

    3
   / \
  9  20
    /  \
   15   7
'''

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#O(N)
def buildTree(preorder, inorder):
    if not preorder or not inorder: return None

    curval = preorder[0]
    curidx = inorder.index(curval)

    root = TreeNode(curval)
    root.left = buildTree(preorder[1:curidx + 1], inorder[:curidx])
    root.right = buildTree(preorder[curidx + 1:], inorder[curidx + 1:])
    return root