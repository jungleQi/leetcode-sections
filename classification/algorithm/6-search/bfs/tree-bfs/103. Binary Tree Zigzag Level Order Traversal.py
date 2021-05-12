#coding=utf-8

'''
Given a binary 3tree, return the zigzag level order traversal of its nodes' values.
 (ie, from left to right, then right to left for the next level and alternate between).
'''
import collections

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

#BFS,按层遍历，
def zigzagLevelOrder_BFS(root):
    ret = []
    q = collections.deque([root])
    while q:
        cnt = len(q)
        cur = []
        while cnt:
            node = q.popleft()
            cnt -= 1

            if(len(ret)%2):
                cur.append(node.val)
            else:
                cur.insert(0, node.val)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        ret.append(cur)

    return ret