def getLength(self, root):
    if root == None:
        return 0
    return self.getLength(root.left) + 1

def countNodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root == None: return 0
    left = getLength(root.left)
    right = getLength(root.right)
    if left == right:
        return 2 ** left + countNodes(root.right)
    else:
        return 2 ** right + countNodes(root.left)


