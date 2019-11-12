'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

1.The root is the maximum number in the array.
2.The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
3.The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructMaximumBinaryTree(nums):
    def splitSubarray(srcarr):
        if len(srcarr) == 1:
            return [],srcarr[0],[]

        maxidx, maxval = 0, srcarr[0]
        for i,num in enumerate(srcarr):
            if num > maxval:
                maxidx = i
                maxval = num
        return srcarr[:maxidx], maxval, srcarr[maxidx+1:]

    def _helper(node, leftArr, rightArr):
        if not leftArr and not rightArr: return

        if leftArr :
            l,v,r = splitSubarray(leftArr)
            node.left = TreeNode(v)
            _helper(node.left, l, r)

        if rightArr:
            l, v, r = splitSubarray(rightArr)
            node.right = TreeNode(v)
            _helper(node.right, l, r)

    l, v, r = splitSubarray(nums)
    node = TreeNode(v)
    _helper(node, l, r)
    return node

nums = [3,2,1,6,0,5]
constructMaximumBinaryTree(nums)