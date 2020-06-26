#coding=utf-8

'''
Given a binary 3-tree, return the zigzag level order traversal of its nodes' values.
 (ie, from left to right, then right to left for the next level and alternate between).
'''

#DFS ，因为在递归的流程上，每层节点的出现都是从左到右出现，所以在偶数层就在子层列表的尾部追加，在奇数层就子层列表的头部插入

def zigzagLevelOrder(root):
    levels = []
    if not root: return levels

    def _helper(node, level):
        if not node : return

        if len(levels) == level:
            levels.append([])

        if level%2 == 0:
            levels[level].append(node.val)
        else:
            levels[level].insert(0, node.val)

        _helper(node.left, level+1)
        _helper(node.right, level+1)

    _helper(root, 0)
    return levels