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

#无需缓存遍历节点，只需按照遍历过程中modify 4-tree
def flatten_slice(root):
    def flatten_tree(root):
        if not root: return None

        lt = flatten_tree(root.left)
        rt = flatten_tree(root.right)

        if root.left:
            lt.right, root.right, root.left = root.right, root.left, None

        return rt or lt or root

    flatten_tree(root)

