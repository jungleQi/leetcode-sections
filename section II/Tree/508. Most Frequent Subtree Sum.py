'''
Given the root of a tree, you are asked to find the most frequent subtree sum.
The subtree sum of a node is defined as the sum of all the node values formed
by the subtree rooted at that node (including the node itself).
So what is the most frequent subtree sum value?
If there is a tie, return all the values with the highest frequency in any order.
'''
import collections,common

def findFrequentTreeSum(root):
    def _helper(node, sumpairs):
        if not node: return 0
        if not node.left and not node.right:
            sumpairs[node.val] += 1
            return node.val

        lsum = _helper(node.left, sumpair)
        rsum = _helper(node.right, sumpair)
        nsum = node.val + lsum + rsum
        sumpairs[nsum] += 1
        return nsum  # very important!!!

    if not root: return []
    sumpair = collections.defaultdict(lambda: 0)
    _helper(root, sumpair)
    pairs = sorted(sumpair.items(), key=lambda x: x[1], reverse=True)

    ret = []
    prev = pairs[0][1]
    for k, v in pairs:
        if v == prev: ret += k,

    return ret

li = [5,14,None,1]
tree = common.Tree()
tree.construct(li)
print(findFrequentTreeSum(tree.root))

