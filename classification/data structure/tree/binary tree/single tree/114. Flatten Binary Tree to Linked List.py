#coding=utf-8
'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

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