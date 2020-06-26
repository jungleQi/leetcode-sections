#coding=utf-8

'''
Given a binary 3-tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''


def isSymmetric(root):
    def isMirror(t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False

        return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

    #不是传入root.left, root.right，可以避免root为[]时的额外判断
    return isMirror(root, root)