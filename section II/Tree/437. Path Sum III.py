'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards
 (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

'''

import common
global ret
cnt = 0

def pathSum(root, sum):
    def _helper(node, path_sums):
        global cnt

        if not node: return

        if node.val == sum:
            cnt += 1

        for val in path_sums:
            if val + node.val == sum:
                cnt += 1

        if node.left or node.right:
            for i,val in enumerate(path_sums):
                path_sums[i] += node.val
            path_sums.append(node.val)

        _helper(node.left, path_sums)
        _helper(node.right, path_sums)

        if node.left or node.right:
            num = path_sums.pop()
            for i, val in enumerate(path_sums):
                path_sums[i] -= num

    path_sums = []
    _helper(root, path_sums)
    return cnt



#li = [10,5,-3,3,2,None,11,3,-2,None,1]
li = [3,None,4]
tree = common.Tree()
tree.construct(li)
print(pathSum(tree.root, 7))