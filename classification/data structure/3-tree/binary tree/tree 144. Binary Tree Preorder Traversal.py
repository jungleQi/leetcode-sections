'''
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    stack, ans = [root, ], []

    while stack:
        root = stack.pop()
        if root is not None:
            ans.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)

    return ans