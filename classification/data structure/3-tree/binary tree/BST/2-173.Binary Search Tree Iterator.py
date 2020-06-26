'''
Implement an iterator over a binary search tree (BST).
Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

Note:
1.next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
2.You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
'''

'''
time complex : avarage O(1)

[detail explain]:
next involves two major operations. 
One is where we pop an element from the stack which becomes the next smallest element to return. This is a O(1) operation. 
However, we then make a call to our helper function _inorder_left which iterates over a bunch of nodes. 
This is clearly a linear classify time operation i.e. O(N) in the worst case. This is true.

However, the important thing to note here is that we only make such a call for nodes which have a right child. 
Otherwise, we simply return. 
Also, even if we end up calling the helper function, it won't always process N nodes. 
They will be much lesser. Only if we have a skewed tree would there be N nodes for the root. 
But that is the only node for which we would call the helper function

Thus, the amortized (average) time complexity for this function would still be O(1) which is what the question asks for. 
We don't need to have a solution which gives constant time operations for every call. 
We need that complexity on average and that is what we get.
'''

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        smallest = self.stack.pop()
        if smallest.right:
            self._leftmost_inorder(smallest.right)
        return smallest.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0