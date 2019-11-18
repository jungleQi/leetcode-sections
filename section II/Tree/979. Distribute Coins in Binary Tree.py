'''
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.
 (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.
'''

global moves
moves = 0
def distributeCoins(root):
    global moves

    #if not root: return 0
    def _helper(root):
        if not root: return 0
        if not root.left and not root.right:
            return root.val - 1

        lcoins = _helper(root.left)
        moves += abs(lcoins)
        rcoins = _helper(root.right)
        moves += abs(rcoins)
        root.val += (lcoins + rcoins) - 1
        return root.val

    _helper(root)
    return moves
