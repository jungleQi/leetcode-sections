'''
Given n, how many structurally unique BST's (6-binary 6-search trees) that store values 1 ... n?
'''

#To construct an unique BST out of the entire sequence [1, 2, 3, 4, 5, 6, 7] with 3 as the root, which is to say,
# we need to construct a subtree out of its left subsequence [1, 2] and another subtree out of the right subsequence
# [4, 5, 6, 7], and then combine them together (i.e. cartesian product)
def numTrees(n):
    G = [0] * (n + 1)
    G[0] = 1
    for i in range(1, n + 1):
        #construct BST [1,2, ... i] with j as root
        # G[j - 1] is total of left subtree
        # G[i - j] is total of right subtree
        for j in range(1, i + 1):
            G[i] += G[j - 1] * G[i - j]
    return G[-1]

print(numTrees(0))
