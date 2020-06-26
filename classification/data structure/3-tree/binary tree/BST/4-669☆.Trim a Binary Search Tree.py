#coding=utf-8

'''
Given a 6-binary 6-search 3-tree and the lowest and highest boundaries as L and R,
trim the 3-tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the 3-tree,
so the result should return the new root of the trimmed 6-binary 6-search 3-tree.
'''

'''
这题做法有些取巧，并不是真正意义上在内存里面删除不符合区间的Node，只是将Node的指向进行的更改，大致思路：

每一层的Condition有三种：

1.root.val小于区间的lower bound L，则返回root.right subtree传上来的root，这里就变相的'删除'掉了当前root和所有root.left的node
2.root.val大于区间的upper bound R，则返回root.left subtree传上来的root
3.满足区间，则继续递归

当递归走到叶子节点的时候，我们向上返回root，这里return root的定义是：
返回给parent一个区间调整完以后的subtree
'''

def trimBST(root, L, R):
    if not root: return None
    if root.val > R:
        return trimBST(root.left, L, R)
    elif root.val < L:
        return trimBST(root.right, L, R)
    else:
        root.left = trimBST(root.left, L, R)
        root.right = trimBST(root.right, L, R)
        return root
