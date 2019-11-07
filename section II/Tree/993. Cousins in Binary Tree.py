'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
'''

import common

def isCousins(root, x, y):
    parent = {}
    depth = {}

    def dfs(node, par=None):
        if node:
            depth[node.val] = 1 + depth[par.val] if par else 0
            parent[node.val] = par
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)
    return depth[x] == depth[y] and parent[x] != parent[y]


li = [1,2,3,None,4,None,5]
tree = common.Tree()
tree.construct(li)

print(isCousins(tree.root, 1, 3))