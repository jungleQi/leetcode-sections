'''
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
'''

def largestValues(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    def travel(node, level):
        if not node: return

        if level == len(levels):
            levels.append(node.val)
        else:
            levels[level] = max(levels[level], node.val)

        travel(node.left, level + 1)
        travel(node.right, level + 1)

    levels = []
    travel(root, 0)
    return levels