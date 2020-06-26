#coding=utf-8

'''
Given a binary 3-tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#dfs，因为递归，所以遍历方式其实是深度优先遍历。
# 只是在遍历过程中，list以层数为索引，为每个节点指定所在层数索引，
# 从将每个节点append到对应的层级子列表

def rightSideView(root):
    levels = []

    def _helper(node, level):
        if not node: return

        if level == len(levels):
            levels.append([])
        levels[level].append(node.val)
        _helper(node.left, level + 1)
        _helper(node.right, level + 1)

    _helper(root, 0)
    print(levels)
    ans = [item[-1] for item in levels]
    return ans

#bfs，通过队列，对tree实现真正的广度优先遍历，元素就是按照每一层从左到右的方式推入队列

import collections
def rightSideView_BFS(root):
    rightmost = dict()
    maxdepth = -1

    deque = collections.deque([(root, 0)])
    while deque:
        node, curdepth = deque.popleft()
        if not node: continue

        maxdepth = max(maxdepth, curdepth)
        rightmost[curdepth] = node.val
        deque.append((node.left, curdepth+1))
        deque.append((node.right, curdepth+1))

    return [rightmost[i] for i in range(maxdepth+1)]
