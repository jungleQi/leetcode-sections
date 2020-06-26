#coding=utf-8

'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
'''


def connect_recursive(root):
    """
    :type root: Node
    :rtype: Node
    """
    if not root: return None

    if root.left:
        root.left.next = root.right
        root.right.next = None

        #here is lightspot!
        if root.next:
            root.right.next = root.next.left

        connect_recursive(root.left)
        connect_recursive(root.right)

    return root

#nice!!
def connect_iterative(root):
    ret = root
    while root and root.left:
        next = root.left
        while root:
            root.left.next = root.right
            #same as recursive's lightspot
            root.right.next = root.next and root.next.left
            root = root.next
        root = next
    return ret