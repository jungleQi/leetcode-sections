from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def show(self):
        return

    def construct(self, li=None):
        if not li:
            return None
        tl = []
        for i in li:
            if i is None:
                tl.append(None)
            else:
                tl.append(TreeNode(i))
        for idx in range(len(li) / 2):
            if idx * 2 + 1 < len(tl) and tl[idx * 2 + 1]:
                tl[idx].left = tl[idx * 2 + 1]

            if idx * 2 + 2 < len(tl) and tl[idx * 2 + 2]:
                tl[idx].right = tl[idx * 2 + 2]
        self.root = tl[0]

    def preOrder(self, cur):
        if not cur:
            return
        print(cur.val)
        self.preOrder(cur.left)
        self.preOrder(cur.right)

    def inOrder(self, cur):
        if not cur:
            return
        self.inOrder(cur.left)
        print(cur.val)
        self.inOrder(cur.right)

    def postOrder(self, cur):
        if not cur:
            return
        self.postOrder(cur.left)
        self.postOrder(cur.right)
        print(cur.val)

    def levelOrder(self, cur):
        dq = deque()
        dq.append(cur)
        while dq:
            tmp = dq.popleft()
            if not tmp:
                continue
            print(tmp.val)
            dq.append(tmp.left)
            dq.append(tmp.right)

'''
l = [2, 3, 4, 5, None, 7]
t = Tree()
t.construct(l)
print("pre order:")
t.preOrder(t.root)
print("in order:")
t.inOrder(t.root)
print("post order:")
t.postOrder(t.root)
print("level order:")
t.levelOrder(t.root)
'''

# [5,4,8,11,null,13,4,7,2,null,null,null,1] error