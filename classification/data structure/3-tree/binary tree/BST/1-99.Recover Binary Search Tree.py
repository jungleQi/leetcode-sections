'''
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Example 1:
Input: [1,3,null,null,2]

   1
  /
 3
  \
   2
Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
'''


def recoverTree(root):
    """
    :type root: TreeNode
    :rtype: None Do not return anything, modify root in-place instead.
    """
    def dfs(root, ret):
        if not root: return
        dfs(root.left, ret)
        ret.append(root.val)
        dfs(root.right, ret)

    def swap(root, one, two):
        if not root: return

        if root.val == one:
            root.val = two
        elif root.val == two:
            root.val = one

        swap(root.left, one, two)
        swap(root.right, one, two)

    nums = []
    dfs(root, nums)

    one, two = nums[0], nums[0]
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            if one == two:
                one = nums[i - 1]
            two = nums[i]
    swap(root, one, two)