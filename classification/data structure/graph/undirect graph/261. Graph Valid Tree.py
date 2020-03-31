#coding=utf-8

'''
Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

Example 1:
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true

Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0,1] is the same as [1,0] and thus will not appear together in edges.
'''

#1.为每个node建立邻接表，即node:neighbors的对应关系

#2.dfs遍历，用visitor记录以遍历过的节点集合，preNode记录当前curNode的根节点

#3.有两种情况导致会再次访问某个节点：
#  3.1 因为连接的双向性，neighbor节点返回来访问cur节点，这种情况就continue跳过，继续展开分支节点进行遍历
#  3.2 环的出现，这种情况就立即返回False

#4.返回：4.1 某个条件判断结果为False，就返回False
#       4.2 根据递归树的返回特点，当前递归结果为False，就立即返回False，这样会结束整个递归返回False
#       4.3 如果所有递归完成都没有返回，就在递归函数最后返回True

import collections
def validTree(n, edges):
    adjacent = [[] for _ in range(n)]
    for edge in edges:
        adjacent[edge[0]].append(edge[1])
        adjacent[edge[1]].append(edge[0])

    def dfs(prev, cur):
        for nei in adjacent[cur]:
            # 坑：如果不放在 A = [if nei in visitor] 之前 进行判断，A就会出现误判而返回
            if nei == prev: continue
            if nei in visitor: return False

            visitor.add(nei)
            ret = dfs(cur, nei)
            if not ret: return False
        return True

    # 定义在外部，嵌套函数也可以操作访问
    visitor = set([0])
    return dfs(-1, 0) and len(visitor) == n

n = 5
edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
print(validTree(n, edges))