#coding=utf-8

#Binary tree could be constructed from preorder/postorder and inorder traversal.
#Inorder traversal of BST is an array sorted in the ascending order: inorder = sorted(preorder).

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []

        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def helper(inorder, postorder):
            if not inorder: return None

            val = postorder[-1]
            idx = inorder.index(val)

            root = TreeNode(val)
            root.left = helper(inorder[:idx], postorder[:idx])
            # 起始是正索引，终止是负索引的用法是OK的
            root.right = helper(inorder[idx + 1:], postorder[idx:-1])

            return root

        postdata = [int(x) for x in data.split(' ') if x]
        indata = sorted(postdata)

        return helper(indata, postdata)
