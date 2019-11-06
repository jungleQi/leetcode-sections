'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
'''

import common,math,collections
def averageOfLevels(root):

    def _traverse(root, level, level_nums):
        if not root: return
        level_nums[level].append(root.val)
        _traverse(root.left, level+1, level_nums)
        _traverse(root.right, level+1, level_nums)

    level_nums = collections.defaultdict(list)
    _traverse(root, 0, level_nums)

    ans = [0]*len(level_nums.keys())
    for level, nums in level_nums.items():
        ans[level] = float(sum(nums))/len(nums)
    return ans


li = [3,9,20,15,7]
tree = common.Tree()
tree.construct(li)
print(averageOfLevels(tree.root))