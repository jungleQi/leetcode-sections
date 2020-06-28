#annotate parent
#coding=utf-8

'''
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.
The answer can be returned in any order.

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.
'''
import collections


#1.DFS让所有节点都增加parent
#2.以target为起点，进行BFS
def distanceK(root, target, K):
    """
    :type root: TreeNode
    :type target: TreeNode
    :type K: int
    :rtype: List[int]
    """
    def dfs(node, par=None):
        if node:
            node.par = par
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)
    deque = collections.deque([[target, 0]])
    seen = {target}
    while deque:
        if deque[0][1] == K:
            return [node.val for node, d in deque]

        node, d = deque.popleft()
        for nei in (node.left, node.right, node.par):
            if nei and nei not in seen:
                deque.append([nei, d + 1])
                seen.add(nei)
    return []