from utils import *

import collections
def cloneGraph(node):
    visitor = {}
    deque = collections.deque([node])
    visitor[node] = Node(node.val, [])
    while deque:
        curNode = deque.popleft()
        for nei in curNode.neighbors:
            if nei not in visitor:
                deque.append(nei)
                visitor[nei] = Node(nei.val, [])
            visitor[curNode].neighbors.append(visitor[nei])
    return visitor[node]





