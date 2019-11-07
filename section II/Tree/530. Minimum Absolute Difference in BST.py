'''
Given a binary search tree with non-negative values,
find the minimum absolute difference between values of any two nodes.
'''
import common

def getMinimumDifference(root):
    def _helper(node, res):
        if node is None: return

        _helper(node.left, res)
        res += node.val,
        _helper(node.right, res)

    res = []
    _helper(root, res)

    minAbl = res[1]-res[0]
    for i in range(2, len(minAbl)):
        minAbl = min(res[i]-res[i-1], minAbl)

    return minAbl

li = [1,None,3,2]
tree = common.Tree()
tree.construct(li)

getMinimumDifference(tree.root)