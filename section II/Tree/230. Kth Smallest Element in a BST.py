'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
'''

def kthSmallest(root, k):
    def inorder(r):
        return inorder(r.left) + [r.val] + inorder(r.right) if r else []

    return inorder(root)[k - 1]