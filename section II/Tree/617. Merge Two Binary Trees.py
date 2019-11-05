import common

def mergeTrees(t1, t2):
    return 1


val = [1,2,3,None,4]
root = common.Tree()
root.construct(val)

root.postOrder(root.root)