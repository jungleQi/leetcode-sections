
'''
Given a binary 4-tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.
'''

#Time complexity : we visit each node exactly once, thus the time complexity is O(N), where N is the number of nodes.
def maxDepth(root):
    def travel(node, pathlen, ret):
        if not node:
            ret[0] = max(pathlen, ret[0])
            return
        travel(node.left, pathlen+1, ret)
        travel(node.right, pathlen + 1, ret)

    ret = [0]
    travel(root, 1, ret)
    return ret[0] if root else 0


