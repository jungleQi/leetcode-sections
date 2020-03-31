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
def cloneGraph_recursive(node):
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
        clone_node.neighbors = [cloneGraph_recursive(n) for n in node.neighbors]

    return clone_node


#防坑：注意建立旧node和新node的时机：
# 1. 在旧node入列queue之后，紧接着建立visitor[oldNode] = newNode的映射是可靠的
# 2. 在deque.pop得到的oldNode,建立旧新节点的映射，存在已有新topo结构被覆盖的问题

import collections
def cloneGraph_solution(node):
    if not node: return node

    # Dictionary to save the visited node and it's respective clone
    # as key and value respectively. This helps to avoid cycles.
    visited = {}
    queue = collections.deque([node])
    visited[node] = Node(node.val, [])

    while queue:
        n = queue.popleft()
        for neighbor in n.neighbors:
            if neighbor not in visited:
                # Clone the neighbor and put in the visited, if not present already
                visited[neighbor] = Node(neighbor.val, [])
                queue.append(neighbor)
            # Add the clone of the neighbor to the neighbors of the clone node "n".
            visited[n].neighbors.append(visited[neighbor])

    # Return the clone of the node from visited.
    return visited[node]

def cloneGraph_ERROR(node):
    visitor = {}
    deque = collections.deque([node])
    while deque:
        curNode = deque.popleft()
        #[2]. 但是，将[1]中nei对应原有的新nei覆盖掉，使nei的后续拓扑断裂
        visitor[curNode] = Node(node.val, [])

        for nei in curNode.neighbors:
            if nei not in visitor:
                deque.append(nei)
                visitor[nei] = Node(nei.val, [])
            #[1]. 此刻，nei 的新复制对象，进入了新curNode的邻居列表
            visitor[curNode].neighbors.append(visitor[nei])
    return visitor[node]


