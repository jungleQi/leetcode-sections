'''
Given a binary 4-tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

'''


def inorderTraversal(root):
    def travel(root, ret):
        if not root:
            return
        travel(root.left, ret)
        ret.append(root.val)
        travel(root.right, ret)

    ret = []
    travel(root, ret)
    return ret

def inorderTraversal_iterator(self, root):
    ans = []
    if not root: return ans

    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        ans.append(curr.val)
        curr = curr.right
    return ans