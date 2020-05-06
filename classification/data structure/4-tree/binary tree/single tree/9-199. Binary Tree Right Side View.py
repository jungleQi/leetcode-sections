'''
Given a binary 4-tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \    /
  5  1          <---
  \
   6            <---
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#O(n)
def rightSideView(root):
    def travel(root, level, path):
        #judge if level is already visited
        if not root or path.get(level, None) is not None:
            return

        path[level] = root.val

        #lightspot: the right-left sequence is nice!!
        travel(root.right, level+1, path)
        travel(root.left, level + 1, path)

    path = dict()
    travel(root, 0, path)
    return path.values()