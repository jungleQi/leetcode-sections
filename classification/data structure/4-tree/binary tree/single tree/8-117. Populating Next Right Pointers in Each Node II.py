'''
Given a binary tree

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
1.You may only use constant extra space.
2.Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
'''

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    """
    :type root: Node
    :rtype: Node
    """
    ans = root
    while root:
        #the sentinel is lightspot
        sentinel = Node(-1)

        curr = sentinel
        while root:
            if root.left:
                curr.next = root.left
                curr = curr.next
            if root.right:
                curr.next = root.right
                curr = curr.next
            root = root.next

        root = sentinel.next
    return ans