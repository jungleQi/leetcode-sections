#coding=utf-8

'''
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
    In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible.
    It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}),
    and all nodes in the last level ({4, 5, 6}) are as far left as possible.
'''

#总体思路：按照完全二叉树叶子节点编号特点，如果最后一个叶子节点的编号 == 总共节点个数，那就是完全二叉树

#1. 完全二叉树当前节点的编号为i，那么它的左子树编号为2*i，右子树编号为2*i+1
#2. while i<len(nodes)的妙处在于：
#   2.1 nodes在循环体中递增时，它的len值是动态变化的；
#   2.2 另外循环结束之后i的值就是总共节点的个数

def isCompleteTree(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root: return True
    nodes = [(root, 1)]
    i = 0
    while i < len(nodes):
        node, v = nodes[i]
        i += 1
        if node.left:
            nodes.append((node.left, 2 * v))
        if node.right:
            nodes.append((node.right, 2 * v + 1))

    return nodes[-1][1] == i