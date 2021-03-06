class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class List(object):
    def __init__(self, arr):
        self.head = None
        if not arr: return
        cur, pre = None, None
        for n in arr:
            if not pre:
                self.head = pre = ListNode(n)
            else:
                cur = ListNode(n)
                pre.next = cur
                pre = cur

    def printList(self, head):
        curNode = head
        while curNode:
            print(curNode.val)
            curNode = curNode.next


class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

