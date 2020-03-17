'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

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

#time complex: O(N)
def buildTree(inorder, postorder):
    if not inorder or not postorder: return None

    curval = postorder[-1]
    curidx = inorder.index(curval)

    root = TreeNode(curval)
    root.left = buildTree(inorder[:curidx], postorder[:curidx])
    root.right = buildTree(inorder[curidx + 1:], postorder[curidx:-1])
    return root