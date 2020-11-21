def zigzagLevelOrder(root):
    def helper(cur, level, ret):
        if not cur: return
        if level == len(ret):
            ret.append([])
        if level%2 == 0:
            ret[level].append(cur.val)
        else:
            ret[level].insert(0, cur.val)

        helper(cur.left, level+1, ret)
        helper(cur.right, level + 1, ret)

    ret = []
    helper(root, 0, ret)
    return ret