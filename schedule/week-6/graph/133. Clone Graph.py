#coding=utf-8
'''
Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:
    For simplicity sake, each node's value is the same as the node's index (1-indexed).
    For example, the first node with val = 1, the second node with val = 2, and so on.
    The graph is represented in the test case using an adjacency list.

Adjacency list is a collection of unordered lists used to represent a finite graph.
Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1.
You must return the copy of the given node as a reference to the cloned graph.

Example:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

'''

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

import collections

def cloneGraph_solution(node):
    """
    :type node: Node
    :rtype: Node
    """
    if not node:
        return node

    # Dictionary to save the visited node and it's respective clone
    # as key and value respectively. This helps to avoid cycles.
    visited = {}

    # Put the first node in the queue
    queue = collections.deque([node])
    # Clone the node and put it in the visited dictionary.
    visited[node] = Node(node.val, [])

    # Start BFS traversal
    while queue:
        # Pop a node say "n" from the from the front of the queue.
        n = queue.popleft()
        # Iterate through all the neighbors of the node
        for neighbor in n.neighbors:
            if neighbor not in visited:
                # Clone the neighbor and put in the visited, if not present already
                visited[neighbor] = Node(neighbor.val, [])
                # Add the newly encountered node to the queue.
                queue.append(neighbor)
            # Add the clone of the neighbor to the neighbors of the clone node "n".
            visited[n].neighbors.append(visited[neighbor])

    # Return the clone of the node from visited.
    return visited[node]

#1.遍历无向图，要记住访问过的Node，这些Node不能再次进入deque
#2.若要双向连通，记住V对象，当U对象反连V时，提取V对象加入到U的邻域对象列表
def cloneGraph_bfs(node):
    if not node: return None

    deque = collections.deque([node])
    head = Node(node.val)
    map = {node.val: head}
    visitor = set([node.val])

    while deque:
        oldnode = deque.popleft()
        newnode = map[oldnode.val]
        for neigh in oldnode.neighbors:
            #此处判断，是为了让两个node能够互通，而不会对同一val申请两个不同Node,呈V的连通
            if neigh.val not in map:
                newNeigh = Node(neigh.val)
                map[neigh.val] = newNeigh
            else:
                newNeigh = map[neigh.val]

            newnode.neighbors.append(newNeigh)

            #避免死循环
            if neigh.val not in visitor:
                deque.append(neigh)
                visitor.add(neigh.val)
    return head