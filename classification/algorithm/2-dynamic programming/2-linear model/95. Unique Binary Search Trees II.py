class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generateTrees(n):
    def generate(i,j):
        if i > j:
            return [None]
        if i == j:
            return [TreeNode(i)]

        res = []
        for k in range(i, j+1):
            left = generate(i,k-1)
            right = generate(k+1, j)
            for l in left:
                for r in right:
                    root = TreeNode(k)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res

    if n ==0:
        return []
    else:
        return generate(0,n)