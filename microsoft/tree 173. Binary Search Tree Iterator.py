class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.nodes = []
        self.inorder(root)
        self.N = len(self.nodes)
        self.curidx = 0

    def inorder(self, node):
        if not node: return
        self.inorder(node.left)
        self.nodes.append(node)
        self.inorder(node.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        ans = self.nodes[self.curidx].val
        self.curidx += 1
        return ans

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.curidx >= self.N:
            return False
        else:
            return True