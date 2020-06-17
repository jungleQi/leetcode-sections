#coding=utf-8

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
Follow up: Recursive solution is trivial, could you do it iteratively?
'''


def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # 入栈：遍历左子树链路
    # 出栈：左子树链路遍历完毕
    # 遍历方式： 当前节点curr或者stack非空为第一层，curr左子树链路遍历为第二层，切换curr到右子树，重复以上流程

    stack = []
    ans = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        ans.append(curr.val)
        curr = curr.right
    return ans