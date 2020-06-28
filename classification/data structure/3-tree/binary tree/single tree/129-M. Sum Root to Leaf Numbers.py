'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
'''

def sumNumbers(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def travel(node, num, ret):
        if not node or (not node.left and not node.right):
            ret[0] += num
            return

        if node.left:
            travel(node.left, 10 * num + node.left.val, ret)
        if node.right:
            travel(node.right, 10 * num + node.right.val, ret)

    if not root: return 0

    ret = [0]
    travel(root, root.val, ret)
    return ret[0]