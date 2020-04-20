#coding=utf-8

'''
Given a binary 4-tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary 4-tree [3,9,20,null,null,15,7],
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
    def travel(root, levelIdx, ret):
        if not root: return
        if levelIdx < len(ret):
            ret[levelIdx].append(root.val)
        else:
            ret.append([root.val])

        travel(root.left, levelIdx + 1, ret)
        travel(root.right, levelIdx + 1, ret)

    ret = []
    travel(root, 0, ret)
    return ret