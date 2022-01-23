'''
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
The successor of a node p is the node with the smallest key greater than p.val.
'''

#so nice!!
def inorderSuccessor_iterator(root, p):
    succ = None
    while root:
        if root.val <= p.val:
            root = root.right
        else:
            succ = root
            root = root.left
    return succ

#hard to think
class Solution(object):
    visitor = False

    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        def travel(root, ret):
            if not root or ret[0]: return

            travel(root.left, ret)
            if root.val == p.val:
                self.visitor = True

            if self.visitor and root.val != p.val:
                ret[0] = root
                self.visitor = False
                return

            travel(root.right, ret)

        ret = [None]
        travel(root, ret)
        return ret[0]
