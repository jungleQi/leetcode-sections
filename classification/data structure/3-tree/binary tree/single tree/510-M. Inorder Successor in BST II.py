#coding=utf-8

'''
Given a node in a binary search tree, find the in-order successor of that node in the BST.

If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree.
Each node will have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}

Follow up:
Could you solve it without looking up any of the node's values?
'''

#key points:
#1. If the node has a right child, and hence its successor is somewhere lower in the tree.
# Go to the right once and then as many times to the left as you could. Return the node you end up with.

#2. Node has no right child, and hence its successor is somewhere upper in the tree.
# Go up till the node that is left child of its parent. The answer is the parent.

def inorderSuccessor_recursive(node):
    """
    :type node: Node
    :rtype: Node
    """

    def downTravel(node):
        if not node or not node.left:
            return node

        return downTravel(node.left)

    def upTravel(node, target):
        if not node or node.val > target:
            return node
        return upTravel(node.parent, target)

    if node.right:
        return downTravel(node.right)
    else:
        return upTravel(node, node.val)

def inorderSuccessor(node):
    """
    :type node: Node
    :rtype: Node
    """
    if not node: return None

    # 有右子节点：就是右节点的最左子节点
    if node.right:
        curNode = node.right
        while curNode and curNode.left:
            curNode = curNode.left
        return curNode
    else:  # 没有右子节点，向上找，第一个有左子节点的节点
        curNode = node
        while curNode.parent and curNode.parent.right == curNode:
            curNode = curNode.parent
        return curNode.parent