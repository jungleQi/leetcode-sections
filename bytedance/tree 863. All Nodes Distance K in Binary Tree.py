#annotate parent

import collections
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