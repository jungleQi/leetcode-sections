#coding=utf-8

'''
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

#先序遍历，让根节点按照层级为单位进行存储
def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    def travelLevel(root, level):
        if not root: return

        #这里的判断是关键，非常优雅
        #不然选择用collections.default(list)，会让整个过程变得繁杂
        if level == len(levels):
            levels.append([])

        levels[level].append(root.val)
        travelLevel(root.left, level + 1)
        travelLevel(root.right, level + 1)

    levels = []
    travelLevel(root, 0)
    return levels