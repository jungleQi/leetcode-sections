import common

def mergeTrees(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1

    t1.val += t2.val
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    return t1


val = [1,2,3,None,4]
root = common.Tree()
root.construct(val)

root.postOrder(root.root)