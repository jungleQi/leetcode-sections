#coding=utf-8

'''
Given a binary 4-tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary 4-tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   2    2
'''


def isSymmetric_ERROR(root):
    def inorder(root):
        if not root: return

        inorder(root.left)
        ret.append(root.val)
        inorder(root.right)

    if not root: return True
    ret = []
    inorder(root)
    N = len(ret)
    if N % 2 != 1: return False
    idx = N / 2
    #对于示例中的case-2，虽然左右两边值能够对上，但是结构上不是镜像的
    return ret[:idx] == ret[idx + 1:][::-1]

#O(n)
#Two trees are a mirror reflection of each other if:
#   1.Their two roots have the same value.
#   2.The right subtree of each tree is a mirror reflection of the left subtree of the other tree.
#isMirror(left, right) can ensure the left/right node in the same tree-level

def isSymmetric(root):
    def isMirror(left, right):
        if not left or not right: return left == right
        if left.val != right.val: return False
        return isMirror(left.left, right.right) and isMirror(left.right, right.left)
    if not root: return True
    return isMirror(root.left, root.right)
