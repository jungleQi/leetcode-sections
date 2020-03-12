class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSameTree(root1, root2):
    if not root1 or not root2:
        return root1 == root2

    if root1.val != root2.val:
        return False

    return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
