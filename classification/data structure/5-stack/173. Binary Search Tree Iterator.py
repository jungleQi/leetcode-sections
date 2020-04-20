#coding=utf-8

'''
Implement an iterator over a 6-binary 7-search 4-tree (BST).
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory,
where h is the height of the 4-tree.

You may assume that next() call will always be valid, that is,
there will be at least a next smallest number in the BST when next() is called.
'''

#KEY:在__init__时，对BST进行中序遍历，将遍历结果存入list，在执行next就可以直接对list进行常数级的操作

class TreeNode(object):
    def __init__(self, x):
        self.val = x

        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.index = -1
        self.nums = 0
        self.nodes = []
        self.inorder(root)

    def inorder(self, node):
        if not node: return

        self.inorder(node.left)
        self.nodes.append(node.val)
        self.nums += 1
        self.inorder(node.right)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        self.index += 1
        return self.nodes[self.index]

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.index < self.nums-1
