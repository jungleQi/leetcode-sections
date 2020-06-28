'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """

    def travel(root, path, k, ret):
        if not root.left and not root.right and k == 0:
            ret.append(path)
            return

        if root.left:
            travel(root.left, path + [root.left.val], k - root.left.val, ret)
        if root.right:
            travel(root.right, path + [root.right.val], k - root.right.val, ret)

    ret = []
    if not root: return ret

    travel(root, [root.val], sum - root.val, ret)
    return ret