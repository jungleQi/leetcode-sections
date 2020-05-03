'''
Return the root node of a binary search tree that matches the given preorder traversal.

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
'''

from .....utils import TreeNode

def bstFromPreorder(preorder):
    """
    :type preorder: List[int]
    :rtype: TreeNode
    """
    if not preorder:
        return None

    i = 1
    while i < len(preorder) and preorder[i] < preorder[0]:
        i += 1

    root = TreeNode(preorder[0])
    root.left = bstFromPreorder(preorder[1:i])
    root.right = bstFromPreorder(preorder[i:])
    return root