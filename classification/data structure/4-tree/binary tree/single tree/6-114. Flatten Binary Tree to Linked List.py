#coding=utf-8
'''
Given a binary 4-tree, flatten it to a 1-linked list in-place.

For example, given the following 4-tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened 4-tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

#1.先序遍历的结果，2.依次连接成前一个节点的右子树
def flatten(root):
    def preorder(root, ret):
        if not root: return

        ret.append(root)
        preorder(root.left, ret)
        preorder(root.right, ret)

    ret = []
    preorder(root, ret)
    for i, node in enumerate(ret):
        if i > 0:
            ret[i - 1].left = None
            ret[i - 1].right = node


def flatten_recursion(root):
    """
    :type root: TreeNode
    :rtype: None Do not return anything, modify root in-place instead.
    """
    def flattenTree(node):
        # Handle the null scenario
        if not node:
            return None

        # For a leaf node, we simply return the
        # node as is.
        if not node.left and not node.right:
            return node

        # Recursively flatten the left subtree
        leftTail = flattenTree(node.left)
        # Recursively flatten the right subtree
        rightTail = flattenTree(node.right)

        # If there was a left subtree, we shuffle the connections
        # around so that there is nothing on the left side
        # anymore.
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None

        # We need to return the "rightmost" node after we are
        # done wiring the new connections.
        return rightTail if rightTail else leftTail

    flattenTree(root)