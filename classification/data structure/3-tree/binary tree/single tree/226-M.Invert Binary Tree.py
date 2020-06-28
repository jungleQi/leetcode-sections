'''
Invert a binary tree.

Example:
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

#Since each node in the tree is visited only once, the time complexity is O(n),
# where n is the number of nodes in the tree.
# We cannot do better than that, since at the very least we have to visit each node to invert it.

def invertTree(root):
    if not root: return None

    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
