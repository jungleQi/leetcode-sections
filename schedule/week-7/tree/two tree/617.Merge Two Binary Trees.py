
#Time complexity : O(m). A total of mm nodes need to be traversed.
# Here, m represents the minimum number of nodes from the two given trees.

def mergeTrees(t1, t2):
    def helper(n1, n2):
        if not n2 or not n1: return

        n1.val += n2.val
        if not n1.left:
            n1.left = n2.left
        else:
            helper(n1.left, n2.left)
        if not n1.right:
            n1.right = n2.right
        else:
            helper(n1.right, n2.right)

    if not t1: return t2
    if not t2: return t1
    helper(t1, t2)
    return t1

def mergeTrees(t1, t2):
    if not t1: return t2
    if not t2: return t1
    t1.val += t2.val
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    return t1


