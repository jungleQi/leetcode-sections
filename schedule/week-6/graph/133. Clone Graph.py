class Node(object):
    def __init__(self, val = 0):
        self.val = val
        self.neighbors = []

visited = {}
def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
    if not node: return node
    if node in visited:
        return visited[node]

    clone_node = Node(node.val, [])
    visited[node] = clone_node
    if node.neighbors:
        clone_node.neighbors = [cloneGraph(n) for n in node.neighbors]

    return clone_node
