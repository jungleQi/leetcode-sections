'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
'''

def inorderTraversal_stack(root):
    ret = []
    stack = []

    while root:
        if not root.left:
            ret.append(root.val)
            while not root.right and stack:
                root = stack.pop()
                ret.append(root.val)
            root = root.right
        else:
            stack.append(root)
            root = root.left

    return ret

def inorderTraversal_recursive(root):
    def helper(root, ret):
        if not root: return
        helper(root.left, ret)
        ret.append(root.val)
        helper(root.right, ret)

    ret = []
    helper(root, ret)
    return ret



