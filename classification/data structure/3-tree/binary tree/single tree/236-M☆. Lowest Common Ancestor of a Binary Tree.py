'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
"The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself)."
'''

'''
Algorithm

1.Start traversing the tree from the root node.

2.If the current node itself is one of p or q, we would mark a variable mid 
as True and continue the search for the other node in the left and right branches.

3.If either of the left or the right branch returns True, 
this means one of the two nodes was found below.

4.If at any point in the traversal, any two of the three flags left, right or mid become True, 
this means we have found the lowest common ancestor for the nodes p and q.
'''

#O(n)
def lowestCommonAncestor_slow(root, p, q):
    def travel(root, path, ret):
        if not root:
            return
        if root and root.val in (p.val, q.val):
            ret.append(path + [root])
            # return

        travel(root.left, path + [root], ret)
        travel(root.right, path + [root], ret)

    ret = []
    travel(root, [], ret)
    if len(ret) == 1:
        return ret[0][0]

    i = 0
    minLen = min(len(ret[0]), len(ret[1]))
    while i < minLen and ret[0][i].val == ret[1][i].val:
        i += 1

    return ret[0][i - 1]


def lowestCommonAncestor_grace(root, p, q):
    def recurse_tree(current_node, ret):
        # If reached the end of a branch, return False.
        if not current_node or ret[0]:
            return False

        # Left Recursion
        left = recurse_tree(current_node.left)
        # Right Recursion
        right = recurse_tree(current_node.right)
        # If the current node is one of p or q
        mid = current_node == p or current_node == q
        # If any two of the three flags left, right or mid become True.
        if mid + left + right >= 2:
            ret[0] = current_node

        # Return True if either of the three bool values is True.
        return mid or left or right

    # Traverse the tree
    ret = [None]
    recurse_tree(root, ret)
    return ret[0]
