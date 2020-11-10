import numpy as np

class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

def inorderSuccessor_iterator(root, p):
    succ = None
    while root:
        if root.val <= p.val:
            root = root.right
        else:
            succ = root
            root = root.left
    return succ