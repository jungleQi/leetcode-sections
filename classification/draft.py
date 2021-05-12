import collections

def zigzagLevelOrder(root):
    ret = []
    q = collections.deque([root])
    while q:
        cnt = len(q)
        cur = []
        while cnt:
            node = q.popleft()
            cnt -= 1

            if(len(ret)%2):
                cur.append(node.val)
            else:
                cur.insert(0, node.val)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        ret.append(cur)

    return ret