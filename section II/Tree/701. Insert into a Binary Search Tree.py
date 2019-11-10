'''
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST.
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
You can return any of them.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insertIntoBST(root, val):
    node = root
    while node:
        if val > node.val:
            if node.right is None:
                node.right = TreeNode(val)
                break
            else:
                node = node.right
        else:
            if node.left is None:
                node.left = TreeNode(val)
                break
            else:
                node  = node.left
    if not root:
        root = TreeNode(val)

    return root