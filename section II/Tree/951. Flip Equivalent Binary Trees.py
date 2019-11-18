'''
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.
'''

def flipEquiv(root1, root2):
    if not root1 or not root2:
        return root1 == root2

    if root1.val == root2.val:
        return (flipEquiv(root1.left, root2.left) and flipEquiv(root1.right, root2.right)) or (
                    flipEquiv(root1.left, root2.right) and flipEquiv(root1.right, root2.left))
    else:
        return False