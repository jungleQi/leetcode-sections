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

def inorderSuccessor(node):
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