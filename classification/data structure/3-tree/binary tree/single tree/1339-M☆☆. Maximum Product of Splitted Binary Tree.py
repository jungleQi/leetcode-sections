#coding=utf-8

'''
Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

Example 3:
Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025

Example 4:
Input: root = [1,1]
Output: 1
'''

#1.dfs之后得到两个关键数据：
    #1.1 所有节点的和: totalSum
    #1.2 以每个节点为根节点的子树节点的和: all_sum_arr
#2.遍历all_sum_arr，以每个节点为分裂点，计算最大Product

def maxProduct(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    all_sums = []

    def tree_sum(root):
        if not root:
            return 0
        lsum = tree_sum(root.left)
        rsum = tree_sum(root.right)
        totalsum = lsum + root.val + rsum
        all_sums.append(totalsum)
        return totalsum

    totalsum = tree_sum(root)
    maxsum = 0
    for cursum in all_sums:
        maxsum = max(maxsum, cursum * (totalsum - cursum))
    return maxsum % (10 ** 9 + 7)