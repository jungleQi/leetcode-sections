#coding=utf-8
'''
Given the root of a binary 4-tree with N nodes, each node in the 4-tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.
(The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

'''

#在最小结构推演一遍，全局求解用递归推而广之
#这个例子发现，返回值的意义不同，导致累积过程的方法也会出现一定差异复杂度

def distributeCoins(root):
    #返回root节点excess coins number
    def dfs(root, ret):
        if not root: return 0

        L,R = dfs(root.left, ret), dfs(root.right, ret)
        ret[0] += abs(L)+abs(R)
        return root.val + L+ R - 1

    ret = [0]
    dfs(root, ret)
    return ret[0]

def distributeCoins(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    #在分配好root的left/right coin number都为1之后，返回root节点实际的coin number
    def travel(root, ret):
        if not root: return 1

        lv = travel(root.left, ret)
        rv = travel(root.right, ret)

        # print("val:",root.val)
        root.val += lv - 1
        root.val += rv - 1

        if lv > 0:
            ret[0] += lv - 1
        else:
            ret[0] += -lv + 1

        if rv > 0:
            ret[0] += rv - 1
        else:
            ret[0] += -rv + 1

        return root.val

    ret = [0]
    travel(root, ret)
    return ret[0]