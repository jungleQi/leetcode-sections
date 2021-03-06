#coding=utf-8
'''
Given the root of a binary 3-tree with N nodes, each node in the 3-tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.
(The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

'''


#在最小结构推演一遍，全局求解用递归推而广之
#这个例子发现，返回值的意义不同，导致累积过程的方法也会出现一定差异复杂度

#algorithm
#1.每个根节点遍历完左右子树之后，左右子节点都只保留1个coin之后，多余的coin返回给它们的parent
#在Parent上汇总，保留1个coin在parent后，多余的coin再向上返回
#2.与此同时，需要记录每个节点(左节点，右节点，当前节点)多出的coins数量，累积到ret
def distributeCoins(root):
    def helper(node, ret):
        if not node:
            return 0

        # 返回值：当前节点所需要的coin数目。
        # 如果为正，表示从根节点得到；负，表示赋给根节点
        lc = helper(node.left, ret)
        rc = helper(node.right, ret)
        ret[0] += abs(lc) + abs(rc)

        return lc + rc + 1 - node.val

    ret = [0]
    helper(root, ret)
    return ret[0]

