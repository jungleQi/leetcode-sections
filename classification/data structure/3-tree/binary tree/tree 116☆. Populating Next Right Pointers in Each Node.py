#coding=utf-8

def connect(root):
    """
    :type root: Node
    :rtype: Node
    """
    ret = root
    # 纵向
    while root and root.left:
        # 横向
        leftMost = root.left
        while root:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            root = root.next
        root = leftMost
    return ret