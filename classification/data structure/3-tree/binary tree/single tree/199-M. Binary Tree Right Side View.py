'''
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \    /
  5  1          <---
  \
   6            <---
'''

def rightSideView(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    def helper(root, level, ret):
        if not root: return

        if len(ret) == level:
            ret.append(root.val)

        helper(root.right, level + 1, ret)
        helper(root.left, level + 1, ret)

    ret = []
    helper(root, 0, ret)
    return ret