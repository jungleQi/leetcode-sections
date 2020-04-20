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
   3    3
'''

#O(n)
def isSymmetric(root):
    def isMirror(left, right):
        if not left or not right: return left == right
        if left.val != right.val: return False
        return isMirror(left.left, right.right) and isMirror(left.right, right.left)
    if not root: return True
    return isMirror(root.left, root.right)
